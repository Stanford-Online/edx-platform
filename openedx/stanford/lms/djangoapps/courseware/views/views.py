from edxmako.shortcuts import render_to_string

def get_banner_account_activation_message(url, user):
    """
    Helper to generate the activation banner html.
    """
    if user.is_anonymous():
        return None

    banner_account_activation_message = None
    if not user.is_active:
        banner_account_activation_message = render_to_string(
            url,
            {'email': user.email}
        )
    return banner_account_activation_message