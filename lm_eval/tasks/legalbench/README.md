# LegalBench

### Paper

Title: LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models

Abstract: https://arxiv.org/pdf/2308.11462.pdf

The LegalBench project is an ongoing open science effort to collaboratively curate tasks for evaluating legal reasoning in English large language models (LLMs). The benchmark currently consists of 162 tasks gathered from 40 contributors.

Homepage: https://hazyresearch.stanford.edu/legalbench/


### Citation

```
@misc{guha2023legalbench,
      title={LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models}, 
      author={Neel Guha and Julian Nyarko and Daniel E. Ho and Christopher Ré and Adam Chilton and Aditya Narayana and Alex Chohlas-Wood and Austin Peters and Brandon Waldon and Daniel N. Rockmore and Diego Zambrano and Dmitry Talisman and Enam Hoque and Faiz Surani and Frank Fagan and Galit Sarfaty and Gregory M. Dickinson and Haggai Porat and Jason Hegland and Jessica Wu and Joe Nudell and Joel Niklaus and John Nay and Jonathan H. Choi and Kevin Tobia and Margaret Hagan and Megan Ma and Michael Livermore and Nikon Rasumov-Rahe and Nils Holzenberger and Noam Kolt and Peter Henderson and Sean Rehaag and Sharad Goel and Shang Gao and Spencer Williams and Sunny Gandhi and Tom Zur and Varun Iyer and Zehua Li},
      year={2023},
      eprint={2308.11462},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@article{koreeda2021contractnli,
  title={ContractNLI: A dataset for document-level natural language inference for contracts},
  author={Koreeda, Yuta and Manning, Christopher D},
  journal={arXiv preprint arXiv:2110.01799},
  year={2021}
}
@article{hendrycks2021cuad,
  title={Cuad: An expert-annotated nlp dataset for legal contract review},
  author={Hendrycks, Dan and Burns, Collin and Chen, Anya and Ball, Spencer},
  journal={arXiv preprint arXiv:2103.06268},
  year={2021}
}
@article{wang2023maud,
  title={MAUD: An Expert-Annotated Legal NLP Dataset for Merger Agreement Understanding},
  author={Wang, Steven H and Scardigli, Antoine and Tang, Leonard and Chen, Wei and Levkin, Dimitry and Chen, Anya and Ball, Spencer and Woodside, Thomas and Zhang, Oliver and Hendrycks, Dan},
  journal={arXiv preprint arXiv:2301.00876},
  year={2023}
}
@inproceedings{wilson2016creation,
  title={The creation and analysis of a website privacy policy corpus},
  author={Wilson, Shomir and Schaub, Florian and Dara, Aswarth Abhilash and Liu, Frederick and Cherivirala, Sushain and Leon, Pedro Giovanni and Andersen, Mads Schaarup and Zimmeck, Sebastian and Sathyendra, Kanthashree Mysore and Russell, N Cameron and others},
  booktitle={Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={1330--1340},
  year={2016}
}
@inproceedings{zheng2021does,
  title={When does pretraining help? assessing self-supervised learning for law and the casehold dataset of 53,000+ legal holdings},
  author={Zheng, Lucia and Guha, Neel and Anderson, Brandon R and Henderson, Peter and Ho, Daniel E},
  booktitle={Proceedings of the eighteenth international conference on artificial intelligence and law},
  pages={159--168},
  year={2021}
}
@article{zimmeck2019maps,
  title={Maps: Scaling privacy compliance analysis to a million apps},
  author={Zimmeck, Sebastian and Story, Peter and Smullen, Daniel and Ravichander, Abhilasha and Wang, Ziqi and Reidenberg, Joel R and Russell, N Cameron and Sadeh, Norman},
  journal={Proc. Priv. Enhancing Tech.},
  volume={2019},
  pages={66},
  year={2019}
}
@article{ravichander2019question,
  title={Question answering for privacy policies: Combining computational and legal perspectives},
  author={Ravichander, Abhilasha and Black, Alan W and Wilson, Shomir and Norton, Thomas and Sadeh, Norman},
  journal={arXiv preprint arXiv:1911.00841},
  year={2019}
}
@article{holzenberger2021factoring,
  title={Factoring statutory reasoning as language understanding challenges},
  author={Holzenberger, Nils and Van Durme, Benjamin},
  journal={arXiv preprint arXiv:2105.07903},
  year={2021}
}
@article{lippi2019claudette,
  title={CLAUDETTE: an automated detector of potentially unfair clauses in online terms of service},
  author={Lippi, Marco and Pa{\l}ka, Przemys{\l}aw and Contissa, Giuseppe and Lagioia, Francesca and Micklitz, Hans-Wolfgang and Sartor, Giovanni and Torroni, Paolo},
  journal={Artificial Intelligence and Law},
  volume={27},
  pages={117--139},
  year={2019},
  publisher={Springer}
}
```

### Groups and Tasks

#### Groups

* `legalbench_exact_match`: The multiple-choices tasks which are evaluated using mean accuracy.
* `legalbench_ISSUE_TASKS`: Issue-spotting tasks in which an LLM must determine if a set of facts raise a particular set of legal questions, implicate an area of the law, or are relevant to a specific party.
* `legalbench_RULE_TASKS`: Rule-recall tasks which require the LLM to generate the correct legal rule on an issue in a jurisdiction (e.g., the rule for hearsay in US federal court), or answer a question about what the law in a jurisdiction does/does not permit.
* `legalbench_CONCLUSION_TASKS`: Rule-conclusion tasks which require an LLM to determine the legal outcome of a set of facts under a specified rule.
* `legalbench_INTERPRETATION_TASKS`: Interpretation tasks which require the LLM to parse and understand a legal text (e.g., classifying contractual clauses).
* `legalbench_RHETORIC_TASKS`: Rhetorical-understanding tasks which require an LLM to reason about legal argumentation and analysis (e.g., identifying textualist arguments).

#### Tasks
* `abercrombie`: 1-sentence description of what this particular task does
* `canada_tax_court_outcomes`: 1-sentence description of what this particular task does
* `citation_prediction_classification`: 1-sentence description of what this particular task does
* `consumer_contracts_qa`: 1-sentence description of what this particular task does
* `contract_nli_confidentiality_of_agreement`: 1-sentence description of what this particular task does
* `contract_nli_explicit_identification`: 1-sentence description of what this particular task does
* `contract_nli_inclusion_of_verbally_conveyed_information`: 1-sentence description of what this particular task does
* `contract_nli_limited_use`: 1-sentence description of what this particular task does
* `contract_nli_no_licensing`: 1-sentence description of what this particular task does
* `contract_nli_notice_on_compelled_disclosure`: 1-sentence description of what this particular task does
* `contract_nli_permissible_acquirement_of_similar_information`: 1-sentence description of what this particular task does
* `contract_nli_permissible_copy`: 1-sentence description of what this particular task does
* `contract_nli_permissible_development_of_similar_information`: 1-sentence description of what this particular task does
* `contract_nli_permissible_post-agreement_possession`: 1-sentence description of what this particular task does
* `contract_nli_return_of_confidential_information`: 1-sentence description of what this particular task does
* `contract_nli_sharing_with_employees`: 1-sentence description of what this particular task does
* `contract_nli_sharing_with_third-parties`: 1-sentence description of what this particular task does
* `contract_nli_survival_of_obligations`: 1-sentence description of what this particular task does
* `contract_qa`: 1-sentence description of what this particular task does
* `corporate_lobbying`: 1-sentence description of what this particular task does
* `cuad_affiliate_license-licensee`: 1-sentence description of what this particular task does
* `cuad_affiliate_license-licensor`: 1-sentence description of what this particular task does
* `cuad_anti-assignment`: 1-sentence description of what this particular task does
* `cuad_audit_rights`: 1-sentence description of what this particular task does
* `cuad_cap_on_liability`: 1-sentence description of what this particular task does
* `cuad_change_of_control`: 1-sentence description of what this particular task does
* `cuad_competitive_restriction_exception`: 1-sentence description of what this particular task does
* `cuad_covenant_not_to_sue`: 1-sentence description of what this particular task does
* `cuad_effective_date`: 1-sentence description of what this particular task does
* `cuad_exclusivity`: 1-sentence description of what this particular task does
* `cuad_expiration_date`: 1-sentence description of what this particular task does
* `cuad_governing_law`: 1-sentence description of what this particular task does
* `cuad_insurance`: 1-sentence description of what this particular task does
* `cuad_ip_ownership_assignment`: 1-sentence description of what this particular task does
* `cuad_irrevocable_or_perpetual_license`: 1-sentence description of what this particular task does
* `cuad_joint_ip_ownership`: 1-sentence description of what this particular task does
* `cuad_license_grant`: 1-sentence description of what this particular task does
* `cuad_liquidated_damages`: 1-sentence description of what this particular task does
* `cuad_minimum_commitment`: 1-sentence description of what this particular task does
* `cuad_most_favored_nation`: 1-sentence description of what this particular task does
* `cuad_no-solicit_of_customers`: 1-sentence description of what this particular task does
* `cuad_no-solicit_of_employees`: 1-sentence description of what this particular task does
* `cuad_non-compete`: 1-sentence description of what this particular task does
* `cuad_non-disparagement`: 1-sentence description of what this particular task does
* `cuad_non-transferable_license`: 1-sentence description of what this particular task does
* `cuad_notice_period_to_terminate_renewal`: 1-sentence description of what this particular task does
* `cuad_post-termination_services`: 1-sentence description of what this particular task does
* `cuad_price_restrictions`: 1-sentence description of what this particular task does
* `cuad_renewal_term`: 1-sentence description of what this particular task does
* `cuad_revenue-profit_sharing`: 1-sentence description of what this particular task does
* `cuad_rofr-rofo-rofn`: 1-sentence description of what this particular task does
* `cuad_source_code_escrow`: 1-sentence description of what this particular task does
* `cuad_termination_for_convenience`: 1-sentence description of what this particular task does
* `cuad_third_party_beneficiary`: 1-sentence description of what this particular task does
* `cuad_uncapped_liability`: 1-sentence description of what this particular task does
* `cuad_unlimited-all-you-can-eat-license`: 1-sentence description of what this particular task does
* `cuad_volume_restriction`: 1-sentence description of what this particular task does
* `cuad_warranty_duration`: 1-sentence description of what this particular task does
* `definition_classification`: 1-sentence description of what this particular task does
* `diversity_1`: 1-sentence description of what this particular task does
* `diversity_2`: 1-sentence description of what this particular task does
* `diversity_3`: 1-sentence description of what this particular task does
* `diversity_4`: 1-sentence description of what this particular task does
* `diversity_5`: 1-sentence description of what this particular task does
* `diversity_6`: 1-sentence description of what this particular task does
* `function_of_decision_section`: 1-sentence description of what this particular task does
* `hearsay`: 1-sentence description of what this particular task does
* `insurance_policy_interpretation`: 1-sentence description of what this particular task does
* `international_citizenship_questions`: 1-sentence description of what this particular task does
* `jcrew_blocker`: 1-sentence description of what this particular task does
* `learned_hands_benefits`: 1-sentence description of what this particular task does
* `learned_hands_business`: 1-sentence description of what this particular task does
* `learned_hands_consumer`: 1-sentence description of what this particular task does
* `learned_hands_courts`: 1-sentence description of what this particular task does
* `learned_hands_crime`: 1-sentence description of what this particular task does
* `learned_hands_divorce`: 1-sentence description of what this particular task does
* `learned_hands_domestic_violence`: 1-sentence description of what this particular task does
* `learned_hands_education`: 1-sentence description of what this particular task does
* `learned_hands_employment`: 1-sentence description of what this particular task does
* `learned_hands_estates`: 1-sentence description of what this particular task does
* `learned_hands_family`: 1-sentence description of what this particular task does
* `learned_hands_health`: 1-sentence description of what this particular task does
* `learned_hands_housing`: 1-sentence description of what this particular task does
* `learned_hands_immigration`: 1-sentence description of what this particular task does
* `learned_hands_torts`: 1-sentence description of what this particular task does
* `learned_hands_traffic`: 1-sentence description of what this particular task does
* `legal_reasoning_causality`: 1-sentence description of what this particular task does
* `maud_ability_to_consummate_concept_is_subject_to_mae_carveouts`: 1-sentence description of what this particular task does
* `maud_financial_point_of_view_is_the_sole_consideration`: 1-sentence description of what this particular task does
* `maud_accuracy_of_fundamental_target_rws_bringdown_standard`: 1-sentence description of what this particular task does
* `maud_accuracy_of_target_general_rw_bringdown_timing_answer`: 1-sentence description of what this particular task does
* `maud_accuracy_of_target_capitalization_rw_(outstanding_shares)_bringdown_standard_answer`: 1-sentence description of what this particular task does
* `maud_additional_matching_rights_period_for_modifications_(cor)`: 1-sentence description of what this particular task does
* `maud_application_of_buyer_consent_requirement_(negative_interim_covenant)`: 1-sentence description of what this particular task does
* `maud_buyer_consent_requirement_(ordinary_course)`: 1-sentence description of what this particular task does
* `maud_change_in_law__subject_to_disproportionate_impact_modifier`: 1-sentence description of what this particular task does
* `maud_changes_in_gaap_or_other_accounting_principles__subject_to_disproportionate_impact_modifier`: 1-sentence description of what this particular task does
* `maud_cor_permitted_in_response_to_intervening_event`: 1-sentence description of what this particular task does
* `maud_cor_permitted_with_board_fiduciary_determination_only`: 1-sentence description of what this particular task does
* `maud_cor_standard_(intervening_event)`: 1-sentence description of what this particular task does
* `maud_cor_standard_(superior_offer)`: 1-sentence description of what this particular task does
* `maud_definition_contains_knowledge_requirement_-_answer`: 1-sentence description of what this particular task does
* `maud_definition_includes_asset_deals`: 1-sentence description of what this particular task does
* `maud_definition_includes_stock_deals`: 1-sentence description of what this particular task does
* `maud_fiduciary_exception__board_determination_standard`: 1-sentence description of what this particular task does
* `maud_fiduciary_exception_board_determination_trigger_(no_shop)`: 1-sentence description of what this particular task does
* `maud_fls_(mae)_standard`: 1-sentence description of what this particular task does
* `maud_general_economic_and_financial_conditions_subject_to_disproportionate_impact_modifier`: 1-sentence description of what this particular task does
* `maud_includes_consistent_with_past_practice`: 1-sentence description of what this particular task does
* `maud_initial_matching_rights_period_(cor)`: 1-sentence description of what this particular task does
* `maud_initial_matching_rights_period_(ftr)`: 1-sentence description of what this particular task does
* `maud_intervening_event_-_required_to_occur_after_signing_-_answer`: 1-sentence description of what this particular task does
* `maud_knowledge_definition`: 1-sentence description of what this particular task does
* `maud_liability_standard_for_no-shop_breach_by_target_non-do_representatives`: 1-sentence description of what this particular task does
* `maud_ordinary_course_efforts_standard`: 1-sentence description of what this particular task does
* `maud_pandemic_or_other_public_health_event__subject_to_disproportionate_impact_modifier`: 1-sentence description of what this particular task does
* `maud_pandemic_or_other_public_health_event_specific_reference_to_pandemic-related_governmental_responses_or_measures`: 1-sentence description of what this particular task does
* `maud_relational_language_(mae)_applies_to`: 1-sentence description of what this particular task does
* `maud_specific_performance`: 1-sentence description of what this particular task does
* `maud_tail_period_length`: 1-sentence description of what this particular task does
* `maud_type_of_consideration`: 1-sentence description of what this particular task does
* `nys_judicial_ethics`: 1-sentence description of what this particular task does
* `opp115_data_retention`: 1-sentence description of what this particular task does
* `opp115_data_security`: 1-sentence description of what this particular task does
* `opp115_do_not_track`: 1-sentence description of what this particular task does
* `opp115_first_party_collection_use`: 1-sentence description of what this particular task does
* `opp115_international_and_specific_audiences`: 1-sentence description of what this particular task does
* `opp115_policy_change`: 1-sentence description of what this particular task does
* `opp115_third_party_sharing_collection`: 1-sentence description of what this particular task does
* `opp115_user_access,_edit_and_deletion`: 1-sentence description of what this particular task does
* `opp115_user_choice_control`: 1-sentence description of what this particular task does
* `oral_argument_question_purpose`: 1-sentence description of what this particular task does
* `overruling`: 1-sentence description of what this particular task does
* `personal_jurisdiction`: 1-sentence description of what this particular task does
* `privacy_policy_entailment`: 1-sentence description of what this particular task does
* `privacy_policy_qa`: 1-sentence description of what this particular task does
* `proa`: 1-sentence description of what this particular task does
* `sara_entailment`: 1-sentence description of what this particular task does
* `successor_liability`: 1-sentence description of what this particular task does
* `scalr`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_best_practice_accountability`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_best_practice_audits`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_best_practice_certification`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_best_practice_training`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_best_practice_verification`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_disclosed_accountability`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_disclosed_audits`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_disclosed_certification`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_disclosed_training`: 1-sentence description of what this particular task does
* `supply_chain_disclosure_disclosed_verification`: 1-sentence description of what this particular task does
* `telemarketing_sales_rule`: 1-sentence description of what this particular task does
* `textualism_tool_dictionaries`: 1-sentence description of what this particular task does
* `textualism_tool_plain`: 1-sentence description of what this particular task does
* `ucc_v_common_law`: 1-sentence description of what this particular task does
* `unfair_tos`: 1-sentence description of what this particular task does



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
