# coding: utf-8

import unittest

from fuzz_introspector_api_client.models.pagination_metadata import PaginationMetadata

class TestPaginationMetadata(unittest.TestCase):
    """PaginationMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationMetadata:
        """Test PaginationMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationMetadata`
        """
        model = PaginationMetadata()
        if include_optional:
            return PaginationMetadata(
                total = 56,
                total_pages = 56,
                first_page = 56,
                last_page = 56,
                page = 56,
                previous_page = 56,
                next_page = 56
            )
        else:
            return PaginationMetadata(
        )
        """

    def testPaginationMetadata(self):
        """Test PaginationMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
