import pytest
from utilities.businessFlows import CustomerFlows
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class TestCase_003_SearchCustomer:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = "Steve"
    lastname = "Gates"

    @pytest.fixture(autouse=True)
    def set_logger(self, request):
        test_name = request.node.name
        self.logger = LogGeneration.loggen(test_name)

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.parametrize("email", ["steve_gates@nopCommerce.com"])
    def test_003_search_customer_by_email(self, setupdriver, email):
        driver = setupdriver
        login = CustomerFlows(driver, self.base_url, self.username, self.password)
        login.login()

        found, name = login.search_customer_by_email(email)

        assert found, "❌ Customer not found"
        print(f"\n✔️ Customer '{name}' found")
        driver.quit()


    @pytest.mark.regression
    def test_003_search_customer_by_name(self, setupdriver):
        driver = setupdriver
        flows = CustomerFlows(driver, self.base_url, self.username, self.password)
        flows.login()

        found, name = flows.search_customer_by_name(self.firstname, self.lastname)

        assert found, "❌ Customer not found"
        print(f"\n✔️ Customer '{name}' found")
        driver.quit()
