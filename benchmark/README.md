# FastAPI Code-Review Benchmark

Twenty paired Python/FastAPI source changes for evaluating git-diff bug detection. Each case contains an original source file in `before/`, its changed version in `after/`, the generated unified Git diff in `change.diff`, and ground truth in `expected.json`. Bug issue line numbers refer to `after/main.py`.

| Case | Bug type | Ground truth |
|---|---|---|
| [`case_01_pagination_off_by_one`](./case_01_pagination_off_by_one/) | Off-by-one pagination | Bug |
| [`case_02_optional_profile_none`](./case_02_optional_profile_none/) | Missing None check | Bug |
| [`case_03_route_auth_removed`](./case_03_route_auth_removed/) | Route authorization removed | Bug |
| [`case_04_stale_invoice_caller`](./case_04_stale_invoice_caller/) | Changed signature with stale caller | Bug |
| [`case_05_swallowed_email_error`](./case_05_swallowed_email_error/) | Swallowed exception | Bug |
| [`case_06_search_sql_injection`](./case_06_search_sql_injection/) | SQL string concatenation | Bug |
| [`case_07_embedded_service_key`](./case_07_embedded_service_key/) | Hardcoded API key | Bug |
| [`case_08_unawaited_inventory_reservation`](./case_08_unawaited_inventory_reservation/) | Missing await | Bug |
| [`case_09_exact_balance_rejected`](./case_09_exact_balance_rejected/) | Wrong comparison operator | Bug |
| [`case_10_unvalidated_upload_filename`](./case_10_unvalidated_upload_filename/) | Input validation removed | Bug |
| [`case_11_unclosed_export_file`](./case_11_unclosed_export_file/) | Unclosed file resource | Bug |
| [`case_12_handler_naming_convention`](./case_12_handler_naming_convention/) | Naming convention drift | Bug |
| [`case_13_extract_price_helper`](./case_13_extract_price_helper/) | Clean helper extraction | Clean |
| [`case_14_rename_user_local`](./case_14_rename_user_local/) | Clean local rename | Clean |
| [`case_15_document_retry_policy`](./case_15_document_retry_policy/) | Clean comment addition | Clean |
| [`case_16_validated_export_filter`](./case_16_validated_export_filter/) | Clean validated feature | Clean |
| [`case_17_suspicious_bounded_limit`](./case_17_suspicious_bounded_limit/) | Clean bounded pagination | Clean |
| [`case_18_permission_helper_extraction`](./case_18_permission_helper_extraction/) | Clean permission refactor | Clean |
| [`case_19_specific_webhook_error`](./case_19_specific_webhook_error/) | Clean exception mapping | Clean |
| [`case_20_optional_status_filter`](./case_20_optional_status_filter/) | Clean suspicious None filter | Clean |
