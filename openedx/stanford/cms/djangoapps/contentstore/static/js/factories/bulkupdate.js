define([
    'domReady', 'jquery', 'gettext'
], function(domReady, $, gettext) {
    'use strict';

    return function(bulkupdateUrl) {
        var $applyMaxAttempts = $('#max-attempts .apply-checkbox'),
            $applyShowAnswer = $('#show-answer .apply-checkbox'),
            $maxAttempts = $('#max-attempts .setting-input'),
            $showAnswer = $('#show-answer .setting-input'),
            $submitBtn = $('.view-bulkupdate .submit-button'),
            $errorMessage = $('.view-bulkupdate .server-message-wrapper .error-server-message'),
            $successMessage = $('.view-bulkupdate .server-message-wrapper .success-server-message'),
            SHOW_ANSWER_OPTIONS = [],
            VALIDATION_ERROR_MESSAGES = {
                nothingSet: gettext('No value set for any field. Please enter a value.'),
                maxAttempts: gettext('MaxAttempts must be a non-negative integer. Please enter a different value.'),
                showAnswer: gettext('Not a valid value for showAnswer. Please enter a different value.')
            };

        // Fill SHOW_ANSWER_OPTIONS with option values from the HTML
        $('#show-answer option').each(function() {
            SHOW_ANSWER_OPTIONS.push($(this).val());
        });

        /**
         * Hides all error and success messages
         */
        function clearFeedbackDisplay() {
            $('.error-message-text').text('');
            $errorMessage.addClass('is-hidden');
            $successMessage.addClass('is-hidden');
        }

        /**
         * Gets setting values from HTML
         * @return {dict} Setting values the user wants changed, empty string
         *                value if they don't want to change that setting
         */
        function getSettingsData() {
            var data = {};
            if ($applyMaxAttempts.is(':checked')) {
                data.maxAttempts = parseInt($maxAttempts.val(), 10);
            } else {
                data.maxAttempts = '';
            }
            if ($applyShowAnswer.is(':checked')) {
                data.showAnswer = $showAnswer.val();
            } else {
                data.showAnswer = '';
            }
            return data;
        }

        /**
         * Validates setting values after being processed by getSettingsData()
         * @param {dict} settings data from getSettingsData()
         * @return {bool} false if no settings changed or settings have invalid value
         */
        function validateData(data) {
            var errors = [],
                errorString = '',
                maxAttempts = data.maxAttempts,
                showAnswer = data.showAnswer;

            if (maxAttempts === '' && showAnswer === '') {
                errors.push(VALIDATION_ERROR_MESSAGES.nothingSet);
            }
            if (maxAttempts && maxAttempts < 0) {
                errors.push(VALIDATION_ERROR_MESSAGES.maxAttempts);
            }
            if (showAnswer && SHOW_ANSWER_OPTIONS.indexOf(showAnswer) < 0) {
                errors.push(VALIDATION_ERROR_MESSAGES.showAnswer);
            }
            if (errors.length > 0) {
                errorString = errors.join(' ');
                $('.error-message-text').text(errorString);
                $errorMessage.removeClass('is-hidden');
                return false;
            }
            return true;
        }

        /**
         * Displays error message on request error
         */
        function onError(response) {
            var errMsg;
            var serverMsg;
            try {
                serverMsg = $.parseJSON(response.responseText) || {};
                errMsg = serverMsg.ErrMsg;
            } catch (e) {
                errMsg = e.message;
            }
            $('.error-message-text').text(errMsg);
            $errorMessage.removeClass('is-hidden');
        }

        /**
         * disables submit button on request completion
         */
        function onComplete() {
            $submitBtn.prop('disabled', false);
        }

        /**
         * Displays success message on request success
         */
        function onSuccess() {
            $successMessage.removeClass('is-hidden');
        }

        /**
         * Gets and validates settings data and makes POST request to BulkUpdate
         */
        function onSubmit() {
            var data = getSettingsData();
            clearFeedbackDisplay();
            if (validateData(data)) {
                $submitBtn.prop('disabled', true);
                $.ajax({
                    type: 'POST',
                    data: data,
                    url: bulkupdateUrl,
                    complete: onComplete,
                    error: onError,
                    success: onSuccess,
                    dataType: 'json'
                });
            }
            return false;
        }

        domReady(function() {
            $submitBtn.click(function(e) {
                e.preventDefault();
                onSubmit(e);
            });

            $maxAttempts.change(function() {
                $applyMaxAttempts.prop('checked', true);
            });
            $showAnswer.change(function() {
                $applyShowAnswer.prop('checked', true);
            });
        });
    };
});
