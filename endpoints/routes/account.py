from endpoints.helpers import RequestHelper
from flask import request, make_response, Blueprint

from lib.models.AccountModel import AccountModel

account = Blueprint('account', __name__)
response = RequestHelper()

@account.route('/account/<acct_num>', methods=['GET'])
def get_account(acct_num):
    """
    Return account data for account number specified
    Args:
        acct_num (str): Account number
    Returns:
        dict ex.
    """
    user_data = AccountModel(acct_num).get_user()
    resp = make_response(
        {
            'data': user_data
        }
    )
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp
