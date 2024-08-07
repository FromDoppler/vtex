from .base_api import BaseApi


class MasterDataApi(BaseApi):
    def _build_url(self, endpoint):
        midpoint = "/api/dataentities/"
        url = self.base_url + midpoint + endpoint
        return url

    def _scroll_url(self):
        url = f"https://{self.account_name}.vtexcommercestable.com.br/api/dataentities/{self.acronym}/scroll"
        return url

    def get_profile_by_email(self, email):
        endpoint = f"CL/search/?_where=email={email}&_fields=_all"
        url = self._build_url(endpoint)
        return self.get_result(url)

    def get_profile_by_user_profile_id(self, user_profile_id):
        endpoint = f"CL/search/?_where=userId={user_profile_id}&_fields=_all"
        url = self._build_url(endpoint)
        return self.get_result(url)

    def get_clients_scroll(self, start_date, end_date, fields, size):
        """
        start_date: STR in the format yyyy-mm-dd
        end_date: STR in the format yyyy-mm-dd
        """
        self.acronym = 'CL'
        url = self._scroll_url() + f"?_fields={fields}&_size={size}"
        if start_date and end_date:
            url += f"&_where=createdIn between {start_date} AND {end_date}"
        result = self.get_result(url)
        return result

    def get_clients_next_scroll(self, token, start_date, end_date, fields, size):
        """
        start_date: STR in the format yyyy-mm-dd
        end_date: STR in the format yyyy-mm-dd
        """
        next_url = self._scroll_url() + f"?_fields={fields}&_size={size}"
        if start_date and end_date:
            next_url += f"&_where=createdIn between {start_date} AND {end_date}&_token={token}"
        return self.get_result(next_url)

    def get_data_entities_list(self):
        url = self.base_url + "/api/dataentities/"
        return self.get_result(url)
    
    def get_data_entity_schema(self, acronym):
        url = self.base_url + f"/api/dataentities/{acronym}/schemas"
        return self.get_result(url)

    def get_data_entity_scroll(self, acronym):
        self.acronym = acronym
        url = self._scroll_url() + "?_size=1000"
        result = self.get_result(url)
        return result

    def get_data_entity_next_scroll(self, token):
        next_url = self._scroll_url() + f"?_token={token}"
        return self.get_result(next_url)
