from django.contrib.auth.models import User
from django.shortcuts import redirect
from social_core.pipeline import partial

from third_party_auth import provider
from third_party_auth.pipeline import AUTH_DISPATCH_URLS
from third_party_auth.pipeline import AUTH_ENTRY_LOGIN
from third_party_auth.pipeline import AUTH_ENTRY_REGISTER


def _dispatch_to_login():
    """
    Redirects to the login page
    """
    return redirect(AUTH_DISPATCH_URLS[AUTH_ENTRY_LOGIN])


def _dispatch_to_register():
    """
    Redirects to the registration page
    """
    return redirect(AUTH_DISPATCH_URLS[AUTH_ENTRY_REGISTER])


@partial.partial
def try_send_existing_lead_to_login(
        strategy,
        auth_entry,
        backend=None,
        user=None,
        social=None,
        current_partial=None,
        allow_inactive_user=False,
        *args,
        **kwargs
):
    def should_force_account_creation():
        """
        For some third party providers, we auto-create user accounts
        """
        current_provider = provider.Registry.get_from_pipeline({
            'backend': current_partial.backend,
            'kwargs': kwargs,
        })
        return (
            current_provider
            and
            (
                current_provider.skip_email_verification
                or
                current_provider.send_to_registration_first
            )
        )

    if not user:
        if auth_entry == AUTH_ENTRY_LOGIN:
            if should_force_account_creation():
                details = kwargs.get('details', {})
                email = details.get('email')
                if email:
                    try:
                        user = User.model.get(email=email)
                    except user.DoesNotExist:
                        return _dispatch_to_register()
                    else:
                        return _dispatch_to_login()
    pass
