# Fuzz Introspector API Client
This is a Python client for the [Fuzz Introspector API](https://introspector.oss-fuzz.com/api), which provides access to query the state of open source fuzzing.

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import fuzz_introspector_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fuzz_introspector_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import fuzz_introspector_api_client
from fuzz_introspector_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fuzz_introspector_api_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with fuzz_introspector_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fuzz_introspector_api_client.Api (api_client)

    try:
        # Temporarily deprecated.
        api_response = api_instance.api_addr_to_recursive_dwarf_info_get()
        print("The response of Api ->api_addr_to_recursive_dwarf_info_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Api ->api_addr_to_recursive_dwarf_info_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Api * | [**api_addr_to_recursive_dwarf_info_get**](docs/Api .md#api_addr_to_recursive_dwarf_info_get) | **GET** /api/addr-to-recursive-dwarf-info | Temporarily deprecated.
*Api * | [**api_all_cross_references_get**](docs/Api .md#api_all_cross_references_get) | **GET** /api/all-cross-references | Returns cross references across the project for a given function.
*Api * | [**api_all_functions_get**](docs/Api .md#api_all_functions_get) | **GET** /api/all-functions | Returns a json representation of all the functions in a given project
*Api * | [**api_all_header_files_get**](docs/Api .md#api_all_header_files_get) | **GET** /api/all-header-files | Gets all the header files in the source code of a given project.
*Api * | [**api_all_jvm_constructors_get**](docs/Api .md#api_all_jvm_constructors_get) | **GET** /api/all-jvm-constructors | Returns a json representation of all the constructors in a given project
*Api * | [**api_all_project_source_files_get**](docs/Api .md#api_all_project_source_files_get) | **GET** /api/all-project-source-files | Returns all source file path in a given project
*Api * | [**api_all_public_candidates_get**](docs/Api .md#api_all_public_candidates_get) | **GET** /api/all-public-candidates | Returns a json representation of all the functions / constructors candidates for further process in a given project.
*Api * | [**api_all_public_classes_get**](docs/Api .md#api_all_public_classes_get) | **GET** /api/all-public-classes | Return a list of public classes in the project.
*Api * | [**api_annotated_cfg_get**](docs/Api .md#api_annotated_cfg_get) | **GET** /api/annotated-cfg | API that returns the annotated  CFG of a project.
*Api * | [**api_branch_blockers_get**](docs/Api .md#api_branch_blockers_get) | **GET** /api/branch-blockers | API that returns the branch blockers of project.
*Api * | [**api_database_language_stats_get**](docs/Api .md#api_database_language_stats_get) | **GET** /api/database-language-stats | Gets stats about line coverage across all languages.
*Api * | [**api_easy_params_far_reach_get**](docs/Api .md#api_easy_params_far_reach_get) | **GET** /api/easy-params-far-reach | API for getting fuzz targets with easy fuzzable arguments.
*Api * | [**api_far_reach_but_low_coverage_get**](docs/Api .md#api_far_reach_but_low_coverage_get) | **GET** /api/far-reach-but-low-coverage | Gets functions with far reach but low code coverage.
*Api * | [**api_far_reach_low_cov_fuzz_keyword_get**](docs/Api .md#api_far_reach_low_cov_fuzz_keyword_get) | **GET** /api/far-reach-low-cov-fuzz-keyword | Returns functions with far reach, low coverage and function names that are often relevant for fuzzing.
*Api * | [**api_full_type_definition_get**](docs/Api .md#api_full_type_definition_get) | **GET** /api/full-type-definition | API that returns the full type definition of a project.
*Api * | [**api_func_debug_types_get**](docs/Api .md#api_func_debug_types_get) | **GET** /api/func-debug-types | Returns a json representation of all the functions in a given project
*Api * | [**api_function_signature_get**](docs/Api .md#api_function_signature_get) | **GET** /api/function-signature | Gets the function signature for a given function.
*Api * | [**api_function_source_code_get**](docs/Api .md#api_function_source_code_get) | **GET** /api/function-source-code | Gets the source code of a given function.
*Api * | [**api_function_target_oracle_get**](docs/Api .md#api_function_target_oracle_get) | **GET** /api/function-target-oracle | Returns a list of function targets based on analysis of all functions in all OSS-Fuzz projects (assuming they have introspetor builds) using several different heuristics.
*Api * | [**api_function_with_matching_return_type_get**](docs/Api .md#api_function_with_matching_return_type_get) | **GET** /api/function-with-matching-return-type | Returns a json representation of all the functions in a given project that match the needed return type
*Api * | [**api_get_all_tests_get**](docs/Api .md#api_get_all_tests_get) | **GET** /api/get-all-tests | Returns the test files of all projects
*Api * | [**api_get_header_files_needed_for_function_get**](docs/Api .md#api_get_header_files_needed_for_function_get) | **GET** /api/get-header-files-needed-for-function | Gets the header files needed for a given function.
*Api * | [**api_get_project_language_from_source_files_get**](docs/Api .md#api_get_project_language_from_source_files_get) | **GET** /api/get-project-language-from-source-files | Gets the project language based on the file extensions of the project
*Api * | [**api_get_target_function_get**](docs/Api .md#api_get_target_function_get) | **GET** /api/get-target-function | Gets details about a specific function.
*Api * | [**api_harness_source_and_executable_get**](docs/Api .md#api_harness_source_and_executable_get) | **GET** /api/harness-source-and-executable | Gets a list of pairs of harness executable/source
*Api * | [**api_jvm_method_properties_get**](docs/Api .md#api_jvm_method_properties_get) | **GET** /api/jvm-method-properties | Returns some properties for the jvm method
*Api * | [**api_ofg_validity_check_get**](docs/Api .md#api_ofg_validity_check_get) | **GET** /api/ofg-validity-check | Returns OFG validity check for all projects.
*Api * | [**api_only_light_with_tests_get**](docs/Api .md#api_only_light_with_tests_get) | **GET** /api/only-light-with-tests | Gets the tests for projects that only have light and not full introspector runs.
*Api * | [**api_optimal_targets_get**](docs/Api .md#api_optimal_targets_get) | **GET** /api/optimal-targets | Returns the list of functions generated by Fuzz Introspector&#39;s analysis &#x60;Optimal Targets&#x60;.
*Api * | [**api_project_repository_get**](docs/Api .md#api_project_repository_get) | **GET** /api/project-repository | Returns the source code repository of a given project.
*Api * | [**api_project_source_code_get**](docs/Api .md#api_project_source_code_get) | **GET** /api/project-source-code | Returns the source code at a specified location for a given project.
*Api * | [**api_project_summary_get**](docs/Api .md#api_project_summary_get) | **GET** /api/project-summary | Returns high-level fuzzing stats of a given project.
*Api * | [**api_project_test_code_get**](docs/Api .md#api_project_test_code_get) | **GET** /api/project-test-code | Extracts source code of a test
*Api * | [**api_project_tests_for_functions_get**](docs/Api .md#api_project_tests_for_functions_get) | **GET** /api/project-tests-for-functions | Gets the tests of a given project.
*Api * | [**api_project_tests_get**](docs/Api .md#api_project_tests_get) | **GET** /api/project-tests | Gets the tests of a given project.
*Api * | [**api_projects_with_light_but_not_full_get**](docs/Api .md#api_projects_with_light_but_not_full_get) | **GET** /api/projects-with-light-but-not-full | Returns projects that have a light introspector but not a full.
*Api * | [**api_sample_cross_references_get**](docs/Api .md#api_sample_cross_references_get) | **GET** /api/sample-cross-references | Gets the source code of functions calling into a given function.
*Api * | [**api_shutdown_get**](docs/Api .md#api_shutdown_get) | **GET** /api/shutdown | Shuts down the server, only if it&#39;s local.
*Api * | [**api_tester_get**](docs/Api .md#api_tester_get) | **GET** /api/tester | Simple response tester.
*Api * | [**api_type_info_get**](docs/Api .md#api_type_info_get) | **GET** /api/type-info | Gets type information about a given type in a project.


## Documentation For Models

 - [Error](docs/Error.md)
 - [PaginationMetadata](docs/PaginationMetadata.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




## Note
This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen