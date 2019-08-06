from edxmako.shortcuts import render_to_string


def get_banner_account_activation_message(user):
    """
    Helper to generate the activation banner html.
    """
    if user.is_anonymous():
        return None

    banner_account_activation_message = None
    if not user.is_active:
        banner_account_activation_message = render_to_string(
            'registration/activate_account_notice.html',
            {'email': user.email}
        )
    return banner_account_activation_message
