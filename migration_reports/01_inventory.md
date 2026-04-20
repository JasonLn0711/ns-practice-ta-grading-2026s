# Migration Inventory

Source grading repo: `/home/jnclaw/every_on_git_jnclaw/planning-everything-track/ns-practice-ta-grading-2026s`

Candidate destination: `/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s`

## Summary

- Files inventoried, excluding `.git`: 276
- Files explicitly linked by parent Markdown scan: 5
- Files covered only by root-level subtree references: 271
- Migration posture: copy first, verify, then create compatibility stubs.

## File Categories

| category | count |
| --- | --- |
| audit_report | 4 |
| automation_script | 18 |
| course_material_metadata | 5 |
| migration_artifact | 9 |
| policy_or_rubric_doc | 13 |
| private_audit_metadata | 58 |
| raw_or_bulky_private_data | 160 |
| repo_metadata_or_index | 2 |
| template | 7 |

## Sensitivity Classes

| sensitivity | count |
| --- | --- |
| course_material_private_or_license_bound | 5 |
| public_safe_within_private_repo | 53 |
| sensitive_unversioned | 160 |
| sensitive_versioned_private_repo | 58 |

## Sensitive Or Private Samples

| relative_path | category | sensitivity | planned_action |
| --- | --- | --- | --- |
| course_materials/hw5/README.md | course_material_metadata | course_material_private_or_license_bound | copy_directly |
| course_materials/hw5/mnist-verification.md | course_material_metadata | course_material_private_or_license_bound | copy_directly |
| course_materials/hw5/raw/.gitkeep | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/01_perceptron_classifier.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/02_neural_network_classifier.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/03_batching.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/04_testing.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/05_Training of Multi-Layer Neural Network.pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/05_development.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/06_drop_out.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/Homework 4 .pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/Homework 5 .pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/circles.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/linearly_separable.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/mnist/readme.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/mnist/t10k-images-idx3-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/mnist/t10k-labels-idx1-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/mnist/train-images-idx3-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/mnist/train-labels-idx1-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/raw/non_linearly_separable.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/rename_map.csv | course_material_metadata | course_material_private_or_license_bound | copy_directly |
| course_materials/hw5/renamed/.gitkeep | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_course_homework04-context-spec.pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_course_homework05-assignment-spec.pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_course_lecture05-training-multi-layer-neural-network.pdf | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_01-perceptron-classifier.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_02-neural-network-classifier.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_03-batching.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_04-testing-hw4-base.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_05-development-configuration.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_06-drop-out.ipynb | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_circles-data.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_linearly-separable-data.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/hw5_reference_non-linearly-separable-data.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/mnist/hw5_reference_mnist_readme.txt | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/mnist/hw5_reference_mnist_test-images-idx3-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/mnist/hw5_reference_mnist_test-labels-idx1-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/mnist/hw5_reference_mnist_train-images-idx3-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw5/renamed/mnist/hw5_reference_mnist_train-labels-idx1-ubyte.gz | raw_or_bulky_private_data | sensitive_unversioned | copy_first_verify_later_keep_ignored |
| course_materials/hw6/README.md | course_material_metadata | course_material_private_or_license_bound | copy_directly |

## Public-Safe Within Private Repo

Docs, scripts, templates, reports, and repository indexes are suitable for
versioning inside the private standalone grading repo. They are not intended to
be public course materials.

## Audit Rule

Every copied file is recorded in `path_mapping.csv` with old path, new path,
sensitivity, planned action, and a short SHA-256 digest.
