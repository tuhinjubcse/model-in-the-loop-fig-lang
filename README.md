# model-in-the-loop-fig-lang

Code and Data for EMNLP 2022 paper <a target="FLUTE: Figurative Language Understanding through Textual Explanations" href="https://arxiv.org/pdf/2205.12404.pdf">FLUTE: Figurative Language Understanding through Textual Explanations</a><br>
Email : tuhin.chakr@cs.columbia.edu ( For enquiries)



You can explore our data at https://huggingface.co/datasets/ColumbiaNLP/FLUTE with dataset explorer<br>
Our train, val and test data can be accessed from files FLUTEfinaltrain.json,FLUTEfinalval.json,FLUTEfinaltest.json
The test labels and explanations for the entire test set are intentionally hidden for now.We will release it in time.Please email us for gold label and explanations for test set

To train the model I->OR model which jointly generates label and rationale<br>


        Download transformers and install it<br>
        Replace the run_translation.py file from here in the folder <i>transformers/examples/pytorch/translation/</i><br>
        Run bash train_I->OR.sh

To get predictions  
        
        Run generateLabel&Explanations.py

To evaluate using automated metrics use
        
                
        See this colab https://colab.research.google.com/drive/1uV26GNlltIlnzRe_IDvVLSmKQsa7yj-7?usp=sharing
        
To access our human eval data look at the folder for humanevaluation
To access our look at modelpredictions folder



                                @inproceedings{Chakrabarty2022FLUTEFL,
                                  title={FLUTE: Figurative Language Understanding through Textual Explanations},
                                  author={Tuhin Chakrabarty and A. Saakyan and Debanjan Ghosh and Smaranda Muresan},
                                  year={2022}
                                }
