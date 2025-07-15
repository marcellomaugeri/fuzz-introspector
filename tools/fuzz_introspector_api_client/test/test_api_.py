# coding: utf-8

import unittest

from fuzz_introspector_api_client.api.api_ import Api
from fuzz_introspector_api_client.configuration import Configuration
from fuzz_introspector_api_client.api_client import ApiClient
from fuzz_introspector_api_client.api_response import ApiResponse
from fuzz_introspector_api_client.exceptions import ApiException
import json

class TestApi (unittest.TestCase):
    """Api  unit test stubs"""

    def setUp(self) -> None:
        self.config = Configuration("https://introspector.oss-fuzz.com", debug=True)
        self.api = Api(ApiClient(self.config))

    def tearDown(self) -> None:
        pass

    def test_api_addr_to_recursive_dwarf_info_get(self) -> None:
        """Test case for api_addr_to_recursive_dwarf_info_get

        Temporarily deprecated.
        """
        pass

    def test_api_all_cross_references_get(self) -> None:
        """Test case for api_all_cross_references_get

        Returns cross references across the project for a given function.
        """
        pass

    def test_api_all_functions_get(self) -> None:
        """Test case for api_all_functions_get

        Returns a json representation of all the functions in a given project
        """
        raw_response = self.api.api_all_functions_get_with_http_info("tinyxml2", _content_type="application/json")
        self.assertEqual(raw_response.status_code, 200)
        body = json.loads(raw_response.raw_data.decode('utf-8'))
        self.assertIsInstance(body, dict)
        self.assertIn('functions', body) # Check if 'functions' key exists
        self.assertIsInstance(body['functions'], list) # Check if 'functions' is a list

    def test_api_all_header_files_get(self) -> None:
        """Test case for api_all_header_files_get

        Gets all the header files in the source code of a given project.
        """
        pass

    def test_api_all_jvm_constructors_get(self) -> None:
        """Test case for api_all_jvm_constructors_get

        Returns a json representation of all the constructors in a given project
        """
        pass

    def test_api_all_project_source_files_get(self) -> None:
        """Test case for api_all_project_source_files_get

        Returns all source file path in a given project
        """
        pass

    def test_api_all_public_candidates_get(self) -> None:
        """Test case for api_all_public_candidates_get

        Returns a json representation of all the functions / constructors candidates for further process in a given project.
        """
        pass

    def test_api_all_public_classes_get(self) -> None:
        """Test case for api_all_public_classes_get

        Return a list of public classes in the project.
        """
        pass

    def test_api_annotated_cfg_get(self) -> None:
        """Test case for api_annotated_cfg_get

        API that returns the annotated  CFG of a project.
        """
        pass

    def test_api_branch_blockers_get(self) -> None:
        """Test case for api_branch_blockers_get

        API that returns the branch blockers of project.
        """
        pass

    def test_api_database_language_stats_get(self) -> None:
        """Test case for api_database_language_stats_get

        Gets stats about line coverage across all languages.
        """
        pass

    def test_api_easy_params_far_reach_get(self) -> None:
        """Test case for api_easy_params_far_reach_get

        API for getting fuzz targets with easy fuzzable arguments.
        """
        pass

    def test_api_far_reach_but_low_coverage_get(self) -> None:
        """Test case for api_far_reach_but_low_coverage_get

        Gets functions with far reach but low code coverage.
        """
        pass

    def test_api_far_reach_low_cov_fuzz_keyword_get(self) -> None:
        """Test case for api_far_reach_low_cov_fuzz_keyword_get

        Returns functions with far reach, low coverage and function names that are often relevant for fuzzing.
        """
        pass

    def test_api_full_type_definition_get(self) -> None:
        """Test case for api_full_type_definition_get

        API that returns the full type definition of a project.
        """
        pass

    def test_api_func_debug_types_get(self) -> None:
        """Test case for api_func_debug_types_get

        Returns a json representation of all the functions in a given project
        """
        pass

    def test_api_function_signature_get(self) -> None:
        """Test case for api_function_signature_get

        Gets the function signature for a given function.
        """
        pass

    def test_api_function_source_code_get(self) -> None:
        """Test case for api_function_source_code_get

        Gets the source code of a given function.
        """
        pass

    def test_api_function_target_oracle_get(self) -> None:
        """Test case for api_function_target_oracle_get

        Returns a list of function targets based on analysis of all functions in all OSS-Fuzz projects (assuming they have introspetor builds) using several different heuristics.
        """
        pass

    def test_api_function_with_matching_return_type_get(self) -> None:
        """Test case for api_function_with_matching_return_type_get

        Returns a json representation of all the functions in a given project that match the needed return type
        """
        pass

    def test_api_get_all_tests_get(self) -> None:
        """Test case for api_get_all_tests_get

        Returns the test files of all projects
        """
        pass

    def test_api_get_header_files_needed_for_function_get(self) -> None:
        """Test case for api_get_header_files_needed_for_function_get

        Gets the header files needed for a given function.
        """
        pass

    def test_api_get_project_language_from_source_files_get(self) -> None:
        """Test case for api_get_project_language_from_source_files_get

        Gets the project language based on the file extensions of the project
        """
        pass

    def test_api_get_target_function_get(self) -> None:
        """Test case for api_get_target_function_get

        Gets details about a specific function.
        """
        pass

    def test_api_harness_source_and_executable_get(self) -> None:
        """Test case for api_harness_source_and_executable_get

        Gets a list of pairs of harness executable/source
        """
        pass

    def test_api_jvm_method_properties_get(self) -> None:
        """Test case for api_jvm_method_properties_get

        Returns some properties for the jvm method
        """
        pass

    def test_api_ofg_validity_check_get(self) -> None:
        """Test case for api_ofg_validity_check_get

        Returns OFG validity check for all projects.
        """
        pass

    def test_api_only_light_with_tests_get(self) -> None:
        """Test case for api_only_light_with_tests_get

        Gets the tests for projects that only have light and not full introspector runs.
        """
        pass

    def test_api_optimal_targets_get(self) -> None:
        """Test case for api_optimal_targets_get

        Returns the list of functions generated by Fuzz Introspector's analysis `Optimal Targets`.
        """
        pass

    def test_api_project_repository_get(self) -> None:
        """Test case for api_project_repository_get

        Returns the source code repository of a given project.
        """
        pass

    def test_api_project_source_code_get(self) -> None:
        """Test case for api_project_source_code_get

        Returns the source code at a specified location for a given project.
        """
        pass

    def test_api_project_summary_get(self) -> None:
        """Test case for api_project_summary_get

        Returns high-level fuzzing stats of a given project.
        """
        pass

    def test_api_project_test_code_get(self) -> None:
        """Test case for api_project_test_code_get

        Extracts source code of a test
        """
        pass

    def test_api_project_tests_for_functions_get(self) -> None:
        """Test case for api_project_tests_for_functions_get

        Gets the tests of a given project.
        """
        pass

    def test_api_project_tests_get(self) -> None:
        """Test case for api_project_tests_get

        Gets the tests of a given project.
        """
        pass

    def test_api_projects_with_light_but_not_full_get(self) -> None:
        """Test case for api_projects_with_light_but_not_full_get

        Returns projects that have a light introspector but not a full.
        """
        pass

    def test_api_sample_cross_references_get(self) -> None:
        """Test case for api_sample_cross_references_get

        Gets the source code of functions calling into a given function.
        """
        pass

    def test_api_shutdown_get(self) -> None:
        """Test case for api_shutdown_get

        Shuts down the server, only if it's local.
        """
        pass

    def test_api_tester_get(self) -> None:
        """Test case for api_tester_get

        Simple response tester.
        """
        pass

    def test_api_type_info_get(self) -> None:
        """Test case for api_type_info_get

        Gets type information about a given type in a project.
        """
        pass


if __name__ == '__main__':
    unittest.main()
