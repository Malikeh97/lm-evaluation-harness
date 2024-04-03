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
* `task_name`: `1-sentence description of what this particular task does`
* `task_name2`: ...

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
