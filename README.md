# model-in-the-loop-fig-lang

Code and Data for EMNLP 2022 paper <b>FLUTE: Figurative Language Understanding through Textual Explanations</b><br>
Email : tuhin.chakr@cs.columbia.edu ( For enquiries)



You can access our data at https://huggingface.co/datasets/ColumbiaNLP/FLUTE<br>
The test labels and explanations for the entire test set are intentionally hidden for now.We will release it in time.Please email us for gold label and explanations for test set
However we have released gold labels and explanations for the part of test set used for evaluation for reproducibility

To train the model I->OR model which jointly generates label and rationale<br>


        Download transformers and install it<br>
        Replace the run_translation.py file from here in the folder <i>transformers/examples/pytorch/translation/</i><br>
        Run bash train_I->OR.sh

To get predictions  
        
        Run generateLabel&Explanations.py

To evaluate using automated metrics use
        
                
        See this colab https://colab.research.google.com/drive/1uV26GNlltIlnzRe_IDvVLSmKQsa7yj-7?usp=sharing
        
To access our human eval data look at the folder for humanevaluation
To access our model predictions look at the folder modelpredictions
 
        @article{chakrabarty2022flute,
          title={FLUTE: Figurative Language Understanding and Textual Explanations},
          author={Chakrabarty, Tuhin and Saakyan, Arkadiy and Ghosh, Debanjan and Muresan, Smaranda},
          journal={arXiv preprint arXiv:2205.12404},
          year={2022}
        }
