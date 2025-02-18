
def test_successful_registration(create_account, customer_account, create_test_data):
    create_account.open_page()
    create_account.fill_in_form(create_test_data['name'], create_test_data['last_name'], create_test_data['email'],
                                create_test_data['password'], create_test_data['password_confirm'])
    customer_account.check_page_title_is('My Account')
    customer_account.check_page_endpoint_is_correct()
    customer_account.check_success_create_msg_is("Thank you for registering with Main Website Store.")


def test_empty_registration_form(create_account):
    create_account.open_page()
    create_account.click_account_button()
    create_account.check_empty_field_messages_count_is(5)
    create_account.check_page_endpoint_is_correct()


def test_incorrect_confirm_password(create_account, create_test_data):
    create_account.open_page()
    create_account.fill_in_form(create_test_data['name'], create_test_data['last_name'], create_test_data['email'],
                                create_test_data['password'], password_confirm='111111')
    create_account.check_password_confirm_error_msg_is("Please enter the same value again.")
    create_account.check_page_endpoint_is_correct()
