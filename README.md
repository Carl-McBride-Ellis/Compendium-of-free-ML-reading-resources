# Compendium of free ML reading resources 
Key: 
* :orange_book: pdf file
* :earth_africa: html book
## ToC
1. [EDA, visualization, and data cleaning](#eda-visualization-and-data-cleaning) (8)
2. [Mathematics for ML](#mathematics-for-ml) (13)
3. [Statistics and probability](#statistics-and-probability) (16)
4. [Optimization](#optimization) (7)
5. [Linear regression](#linear-regression) (6)
6. [Machine learning](#machine-learning) (46)
7. [R realted](#r-realted) (18)
8. [Feature engineering](#feature-engineering) (2)
9. [Explainability/interpretability](#explainabilityinterpretability) (5)
10. [Deep learning / neural networks](#deep-learning--neural-networks) (16)
11. [Reinforcement learning](#reinforcement-learning) (8)
12. [Recommender systems](#recommender-systems) (2)
13. [Anomaly detection](#anomaly-detection) (1)
14. [Computer vision](#computer-vision) (2)
15. [Natural language processing (NLP) and large language models (LLM)](#natural-language-processing-nlp-and-large-language-models-llm) (13)
16. [Causal inference](#causal-inference) (9)
17. [Conformal prediction](#conformal-prediction) (5)
18. [Time series: Forecasting](#time-series-forecasting) (7)

Total number of books: **184**

<sub>Note: All books listed here have been made freely available by their respective authors/publishers, and all [arXiv](https://arxiv.org/) papers are inherently free.</sub>

---
### EDA, visualization, and data cleaning
* :earth_africa: ["Python for Data Analysis (3rd Edition)"](https://wesmckinney.com/book/) by Wes McKinney
* :earth_africa: ["Flexible Imputation of Missing Data"](https://stefvanbuuren.name/fimd/) by Stef van Buuren
* :earth_africa: ["Fundamentals of Data Visualization"](https://clauswilke.com/dataviz/) by Claus O. Wilke
* :earth_africa: ["R Graphics Cookbook"](https://r-graphics.org/) by Winston Chang
* :earth_africa: ["Modern Data Visualization with R"](https://rkabacoff.github.io/datavis/) by Robert Kabacoff
* :orange_book: ["Data Cleaning and Machine Learning: A Systematic Literature Review"](https://arxiv.org/pdf/2310.01765) by Pierre-Olivier Côté, Amin Nikanjam, Nafisa Ahmed, Dmytro Humeniuk, and Foutse Khomh
* :orange_book: ["Think Stats: Exploratory Data Analysis in Python"](https://greenteapress.com/thinkstats2/thinkstats2.pdf) by Allen B. Downey
* :orange_book: ["SQL Notes for Professionals"](https://books.goalkicker.com/SQLBook/SQLNotesForProfessionals.pdf)

---
### Mathematics for ML
* :orange_book: ["Mathematics for Machine Learning"](https://mml-book.github.io/book/mml-book.pdf) by Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong
* :orange_book: ["The Matrix Calculus You Need For Deep Learning"](https://arxiv.org/pdf/1802.01528.pdf) by Terence Parr, and Jeremy Howard
* :orange_book: ["Matrix Analysis"](https://tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf) by Joel A. Tropp
* :orange_book: ["Linear Algebra Done Wrong"](https://www.math.brown.edu/streil/papers/LADW/LADW_2017-09-04.pdf) by Sergei Treil
* :orange_book: ["Linear Algebra Done Right"](https://link.springer.com/content/pdf/10.1007/978-3-031-41026-0.pdf) by Sheldon Axler
* :orange_book: ["Linear Algebra, Theory And Applications"](https://d2orq2otfnmxdd.cloudfront.net/books/Linearalgebra/Linearalgebra.pdf) by Kenneth Kuttler
* :orange_book: ["The Matrix Cookbook"](https://www2.imm.dtu.dk/pubdb/edoc/imm3274.pdf) by Kaare Brandt Petersen, and Michael Syskind Pedersen
* :orange_book: ["Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares"](https://web.stanford.edu/~boyd/vmls/vmls.pdf) by Stephen Boyd and Lieven Vandenberghe
* :orange_book: ["Linear Algebra for Data Science"](https://drive.google.com/file/d/1nJVwdQV9zp-Q9VQenZF0-HOOG6L2lEOD/view) by Wanmo Kang, and Kyunghyun Cho
* :orange_book: ["Linear Algebra for Computer Vision, Robotics, and Machine Learning"](https://www.seas.upenn.edu/~cis5150/linalg-I.pdf) by Jean Gallier and Jocelyn Quaintance
* :orange_book: ["Matrix Calculus (for Machine Learning and Beyond)"](https://arxiv.org/pdf/2501.14787) by Paige Bright, Alan Edelman, Steven G. Johnson
* :orange_book: ["Algebra, Topology, Differential Calculus, and Optimization Theory For Computer Science and Machine Learning"](https://www.cis.upenn.edu/~jean/math-deep.pdf) by Jean Gallier and Jocelyn Quaintance
* :earth_africa: ["Linear Algebra for Data Science with examples in R"](https://shainarace.github.io/LinearAlgebra/index.html) by Shaina Race Bennett

---
### Statistics and probability
* :orange_book: ["Probability and Statistics - The Science of Uncertainty"](https://www.utstat.toronto.edu/mikevans/jeffrosenthal/book.pdf) by Michael J. Evans and Jeffrey S. Rosenthal
* :orange_book: ["Probability in High Dimensions"](https://tropp.caltech.edu/notes/Tro21-Probability-High-LN-corr.pdf) by Joel A. Tropp
* :orange_book: ["Introduction to Probability"](https://drive.google.com/file/d/1VmkAAGOYCTORq1wxSQqy255qLJjTNvBI/edit) by Joseph K. Blitzstein and Jessica Hwang
* :orange_book: ["A History of the Central Limit Theorem From Classical to Modern Probability Theory"](https://www.medicine.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/HistoryCentralLimitTheorem.pdf) by Hans Fischer
* :orange_book: ["Think Bayes: Bayesian Statistics Made Simple"](https://www.greenteapress.com/thinkbayes/thinkbayes.pdf) by Allen B. Downey
* :orange_book: ["Introduction to Bayesian Statistics"](https://www.stat.auckland.ac.nz/~brewer/stats331.pdf) by Brendon J. Brewer
* :orange_book: ["learning statistics with jamovi"](https://davidfoxcroft.github.io/lsj-book/learning-statistics-with-jamovi.pdf) by Danielle J. Navarro and David R. Foxcroft
* :orange_book: ["Bayesian Data Analysis"](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf) by Andrew Gelman, John Carlin, Hal Stern, David Dunson, Aki Vehtari, and Donald Rubin
* :orange_book: ["Compendium of Common Probability Distributions"](https://www.causascientia.org/math_stat/Dists/Compendium.pdf) by Michael P. McLaughlin
* :orange_book: ["Probability and Statistics for Data Science"](https://cims.nyu.edu/~cfgranda/pages/stuff/probability_stats_for_DS.pdf) by Carlos Fernandez-Granda
* :orange_book: ["Statistical Modeling: An Excursion Through 14 Topics"](https://user.math.uzh.ch/furrer/download/sta121/script_sta121.pdf) by Reinhard Furrer
* :orange_book: ["Robust Statistics"](http://parker.ad.siu.edu/Olive/runrob.pdf) by David J. Olive
* :orange_book: ["CS109 Probability for Computer scientists"](https://chrispiech.github.io/probabilityForComputerScientists/en/ProbabilityForComputerScientists.pdf) by Chris Piech
* :orange_book: ["Odds & Ends: Introducing Probability & Decision with a Visual Emphasis"](https://jonathanweisberg.org/vip/_main.pdf) by Jonathan Weisberg
* :orange_book: ["Grinstead and Snell’s Introduction to Probability"](https://math.dartmouth.edu/~prob/prob/prob.pdf) by Peter G. Doyle
* :orange_book: ["High-Dimensional Probability: An Introduction with Applications in Data Science"](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.pdf) by Roman Vershynin

---
### Optimization
* :orange_book: ["Convex Optimization"](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) by Stephen Boyd and Lieven Vandenberghe
* :orange_book: ["An introduction to optimization on smooth manifolds"](https://www.nicolasboumal.net/book/IntroOptimManifolds_Boumal_2023.pdf) by Nicolas Boumal
* :orange_book: ["Lecture Notes: Optimization for Machine Learning"](https://arxiv.org/pdf/1909.03550) by Elad Hazan
* :orange_book: ["A Modern Approach to Teaching an Introduction to Optimization"](https://castle.princeton.edu/wp-content/uploads/2024/01/Powell-MATO-Final-Jan-23-2024.pdf) by Warren B. Powell
* :orange_book: ["Bayesian Optimization"](https://bayesoptbook.com/book/bayesoptbook_a4.pdf) by Roman Garnett
* :orange_book: ["Fundamentals of Optimization Theory With Applications to Machine Learning"](https://www.seas.upenn.edu/~cis5150/linalg-II.pdf) by Jean Gallier and Jocelyn Quaintance
* :orange_book: ["Algorithms for Optimization"](https://algorithmsbook.com/optimization/files/optimization.pdf) by Mykel J. Kochenderfer, and Tim A. Wheeler

---
### Linear regression
* :orange_book: ["The Truth about Linear Regression"](https://www.stat.cmu.edu/~cshalizi/TALR/TALR.pdf) by Cosma Rohilla Shalizi
* :orange_book: ["Lecture notes on Ridge regression"](https://arxiv.org/pdf/1509.09169.pdf) by Wessel N. van Wieringen
* :orange_book: ["Linear Model and Extensions"](https://arxiv.org/pdf/2401.00649.pdf) by Peng Ding
* :orange_book: ["Regression and Other Stories"](https://users.aalto.fi/~ave/ROS.pdf) by Andrew Gelman, Jennifer Hill, and Aki Vehtari
* :orange_book: ["Lecture Notes on High Dimensional Linear Regression"](https://arxiv.org/pdf/2412.15633) by Alberto Quaini
* :earth_africa: ["Analysing Data using Linear Models"](https://bookdown.org/pingapang9/linear_models_bookdown/) by Stéphanie M. van den Berg


---
### Machine learning
* :orange_book: ["An Introduction to Statistical Learning with Applications in Python"](https://hastie.su.domains/ISLP/ISLP_website.pdf.view-in-google.html) by James, Witten, Hastie, Tibshirani, and Taylor
* :orange_book: ["The Elements of Statistical Learning"](https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf.download.html) by Hastie, Tibshirani, and Friedman
* :orange_book: ["Computer Age Statistical Inference: Algorithms, Evidence and Data Science"](https://hastie.su.domains/CASI_files/PDF/casi.pdf.download.html) by Bradley Efron and Trevor Hastie
* :orange_book: ["Pattern Recognition and Machine Learning"](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) by Christopher M. Bishop
* :orange_book: ["Probabilistic Machine Learning: An Introduction"](https://github.com/probml/pml-book/releases/latest/download/book1.pdf) by Kevin Patrick Murphy
* :orange_book: ["Probabilistic Machine Learning: Advanced Topics"](https://github.com/probml/pml2-book/releases/latest/download/book2.pdf) by Kevin Patrick Murphy
* :orange_book: ["Understanding Machine Learning: From Theory to Algorithms"](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/copy.html) by Shai Shalev-Shwartz and Shai Ben-David
* :orange_book: ["Foundations of Machine Learning"](https://www.dropbox.com/s/38p0j6ds5q9c8oe/10290.pdf) by Mehryar Mohri, Afshin Rostamizadeh, and Ameet Talwalkar
* :orange_book: ["Gaussian Processes for Machine Learning"](https://gaussianprocess.org/gpml/chapters/RW.pdf) by Carl Edward Rasmussen and Christopher K. I. Williams
* :orange_book: ["Information Theory, Inference, and Learning Algorithms"](https://www.inference.org.uk/itprnn/book.pdf) by David J. C. MacKay
* :orange_book: ["Mathematical Analysis of Machine Learning Algorithms"](https://tongzhang-ml.org/lt-book/lt-book.pdf) by Tong Zhang
* :orange_book: ["A Comprehensive Guide to Machine Learning"](https://snasiriany.me/files/ml-book.pdf) by Soroush Nasiriany, Garrett Thomas, William Wang, Alex Yang, Jennifer Listgarten, and Anant Sahai
* :orange_book: ["A Course in Machine Learning"](http://ciml.info/dl/v0_99/ciml-v0_99-all.pdf) by Hal Daumé III
* :orange_book: ["Machine Learning - A First Course for Engineers and Scientists"](https://smlbook.org/book/sml-book-draft-latest.pdf) by Andreas Lindholm, Niklas Wahlström, Fredrik Lindsten, and Thomas B. Schön
* :orange_book: ["Automated Machine Learning: Methods, Systems, Challenges"](https://link.springer.com/content/pdf/10.1007/978-3-030-05318-5.pdf) by  Frank Hutter, Lars Kotthoff, and Joaquin Vanschoren
* :orange_book: ["Statistics and Machine Learning in Python"](https://raw.githubusercontent.com/duchesnay/data/master/pdf/StatisticsMachineLearningPython.pdf) by Edouard Duchesnay, Tommy Löfstedt, and Feki Younes
* :orange_book: ["Bayesian Reasoning and Machine Learning"](http://web4.cs.ucl.ac.uk/staff/D.Barber/textbook/200620.pdf) by David Barber
* :orange_book: ["Boosting: Foundations and Algorithms"](https://direct.mit.edu/books/book-pdf/2091763/book_9780262301183.pdf) by  Robert E. Schapire, and Yoav Freund
* :orange_book: ["Algorithms for Decision Making"](https://algorithmsbook.com/files/dm.pdf) by Mykel J. Kochenderfer, Tim A. Wheeler, and Kyle H. Wray
* :orange_book: ["Introduction to Algorithmic Marketing"](https://storage.googleapis.com/algorithmic-marketing-book/algorithmic-marketing-ai-for-marketing-operations-r1.8ga.pdf) by Ilya Katsov
* :orange_book: ["Applied Data Science"](https://columbia-applied-data-science.github.io/appdatasci.pdf) by Ian Langmore, and Daniel Krasner
* :orange_book: ["CS229 Lecture Notes"](https://cs229.stanford.edu/notes2022fall/main_notes.pdf) by Andrew Ng, and Tengyu Ma
* :orange_book: ["Random Matrix Methods for Machine Learning"](https://zhenyu-liao.github.io/pdf/RMT4ML.pdf) by Romain Couillet, and Zhenyu Liao
* :orange_book: ["The Orange Book of Machine Learning"](https://carl-mcbride-ellis.github.io/TOBoML/TOBoML.pdf) by Carl McBride Ellis
* :orange_book: ["Learning Theory from First Principles"](https://www.di.ens.fr/~fbach/ltfp_book.pdf) by Francis Bach
* :orange_book: ["Advanced Data Analysis from an Elementary Point of View"](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a0ec06896e6775d03cf2e905f48616bc2ffadf19) by Cosma Rohilla Shalizi
* :orange_book: ["Machine Learning"](https://www.cs.cmu.edu/~tom/files/MachineLearningTomMitchell.pdf) by Tom Mitchell
* :orange_book: ["Hyperparameter Tuning for Machine and Deep Learning with R: A Practical Guide"](https://link.springer.com/content/pdf/10.1007/978-981-19-5170-1.pdf) Eds.:  Eva Bartz, Thomas Bartz-Beielstein, Martin Zaefferer, and Olaf Mersmann
* :orange_book: ["Foundations of Data Science"](https://www.cs.cornell.edu/jeh/book.pdf) by Avrim Blum, John Hopcroft, and Ravindran Kannan
* :orange_book: ["Machine Learning Systems: Principles and Practices of Engineering Artificially Intelligent Systems"](https://mlsysbook.ai/Machine-Learning-Systems.pdf) by Vĳay Janapa Reddi
* :orange_book: ["Concise Machine Learning"](https://people.eecs.berkeley.edu/~jrs/papers/machlearn.pdf) by Jonathan Richard Shewchuk
* :orange_book: ["Probabilistic Artificial Intelligence"](https://arxiv.org/pdf/2502.05244) by Andreas Krause, and Jonas Hübotter
* :orange_book: ["A Brief Introduction to Machine Learning for Engineers"](https://arxiv.org/pdf/1709.02840.pdf) by Osvaldo Simeone
* :orange_book: ["Machine Learning: The Basics"](https://arxiv.org/pdf/1805.05052) by Alexander Jung
* :orange_book: ["A high-bias, low-variance introduction to Machine Learning for physicists"](https://arxiv.org/pdf/1803.08823) by Pankaj Mehta, Marin Bukov, Ching-Hao Wang, Alexandre G.R. Day, Clint Richardson, Charles K. Fisher, David J. Schwab
* :orange_book: ["Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning"](https://arxiv.org/pdf/1811.12808.pdf) by Sebastian Raschka
* :orange_book: ["Hyper-Parameter Optimization: A Review of Algorithms and Applications"](https://arxiv.org/pdf/2003.05689.pdf) by Tong Yu and Hong Zhu
* :orange_book: ["How to avoid machine learning pitfalls: a guide for academic researchers"](https://arxiv.org/pdf/2108.02497.pdf) by Michael A. Lones
* :orange_book: ["Online Learning: A Comprehensive Survey"](https://arxiv.org/pdf/1802.02871.pdf) by Steven C. H. Hoi, Doyen Sahoo, Jing Lu and Peilin Zhao
* :orange_book: ["Introduction to Machine Learning"](https://arxiv.org/pdf/2409.02668) by Laurent Younes
* :earth_africa: ["Supervised Machine Learning for Science"](https://ml-science-book.com/) by Christoph Molnar, and Timo Freiesleben
* :earth_africa: ["Python Data Science Handbook"](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas
* :earth_africa: ["A Guide on Data Analysis"](https://bookdown.org/mike/data_analysis/) by Mike Nguyen
* :earth_africa: ["Applied Machine Learning for Tabular Data"](https://aml4td.org/) by Max Kuhn, and Kjell Johnson
* :earth_africa: ["Applied Machine Learning in Python: a Hands-on Guide with Code"](https://geostatsguy.github.io/MachineLearningDemos_Book/intro.html) by Michael J. Pyrcz
* :earth_africa: ["Learning Data Science"](https://learningds.org/) by Sam Lau, Joey Gonzalez, and Deb Nolan

---
### [R](https://www.r-project.org/) realted
* :earth_africa: ["Big Book of R"](https://www.bigbookofr.com/) by Oscar Baruffa
* :earth_africa: ["Hands-On Programming with R"](https://rstudio-education.github.io/hopr/) by Garrett Grolemund
* :earth_africa: ["Hands-On Machine Learning with R"](https://bradleyboehmke.github.io/HOML/) by Bradley Boehmke and Brandon Greenwell
* :earth_africa: ["Linear Algebra for Data Science with examples in R"](https://shainarace.github.io/LinearAlgebra/index.html) by Shaina Race Bennett
* :orange_book: ["Deep R Programming"](https://deepr.gagolewski.com/deepr.pdf) by Marek Gagolewski
* :earth_africa: ["Efficient R programming"](https://csgillespie.github.io/efficientR/) by Colin Gillespie, and Robin Lovelace
* :earth_africa: ["R for Data Science"](https://r4ds.hadley.nz/) by Hadley Wickham, Mine Çetinkaya-Rundel, and Garrett Grolemund
* :earth_africa: ["Advanced R"](https://adv-r.hadley.nz/) by Hadley Wickham
* :earth_africa: ["The Epidemiologist R Handbook"](https://epirhandbook.com/en/) editor Neale Batra
* :earth_africa: ["Practical Statistics in Medicine with R"](https://practical-stats-med-r.netlify.app/) by Konstantinos I. Bougioukas
* :earth_africa: ["Text Mining with R: A Tidy Approach"](https://www.tidytextmining.com/) by Julia Silge and David Robinson
* :earth_africa: ["Spatial Statistics for Data Science: Theory and Practice with R"](https://www.paulamoraga.com/book-spatial/) by Paula Moraga
* :earth_africa: ["R Graphics Cookbook"](https://r-graphics.org/) by Winston Chang
* :earth_africa: ["Toolbox for Social Scientists and Policy Analysts: Applied Predictive Analytics with Machine Learning and R"](https://yaydede.github.io/toolbox/) by Yigit Aydede
* :earth_africa: ["Fundamentos de ciencia de datos con R"](https://cdr-book.github.io/index.html) by Gema Fernández-Avilés Calderón y José-María Montero
* :earth_africa: ["Modern Data Visualization with R"](https://rkabacoff.github.io/datavis/) by Robert Kabacoff
* :earth_africa: ["Introduction to Econometrics with R"](https://www.econometrics-with-r.org/) by Christoph Hanck, Martin Arnold, Alexander Gerber, and Martin Schmelzer
* :orange_book: ["The R Inferno"](https://www.burns-stat.com/pages/Tutor/R_inferno.pdf) by Patrick Burns

---
### Feature engineering
* :earth_africa: ["Feature Engineering and Selection: A Practical Approach for Predictive Models"](http://www.feat.engineering/) by Max Kuhn and Kjell Johnson
* :earth_africa: ["Feature Engineering A-Z"](https://feaz-book.com/) by Emil Hvitfeldt

---
### Explainability/interpretability
* :orange_book: ["Trustworthy Machine Learning"](http://trustworthymachinelearning.com/trustworthymachinelearning.pdf) by Kush R. Varshney
* :orange_book: ["Trustworthy Machine Learning: Theory, Applications, Intuitions"](https://twml.cdn.prismic.io/twml/091580bb-9ba5-4821-a80a-d837d4ba1307_Trustworthy+Machine+Learning+book+2023.pdf) by Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, and Seong Joon Oh
* :orange_book: ["A Comprehensive Guide to Explainable AI: From Classical Models to LLMs"](https://arxiv.org/pdf/2412.00800) by Weiche Hsieh, *et al.*
* :earth_africa: ["Interpretable Machine Learning: A Guide for Making Black Box Models Explainable"](https://christophm.github.io/interpretable-ml-book/) by Christoph Molnar
* :earth_africa: ["Explanatory Model Analysis"](https://ema.drwhy.ai/) by Przemyslaw Biecek and Tomasz Burzykowski

---
### Deep learning / neural networks
* :orange_book: ["The Modern Mathematics of Deep Learning"](https://arxiv.org/pdf/2105.04026.pdf) by Julius Berner, Philipp Grohs, Gitta Kutyniok, and Philipp Petersen
* :orange_book: ["Mathematics of Neural Networks"](https://arxiv.org/pdf/2403.04807) by Bart M.N. Smets
* :orange_book: ["The Principles of Deep Learning Theory"](https://arxiv.org/pdf/2106.10165.pdf) by Daniel A. Roberts, Sho Yaida, and Boris Hanin
* :orange_book: ["Machine learning with neural networks"](https://arxiv.org/pdf/1901.05639.pdf) by Bernhard Mehlig
* :orange_book: ["Dive into Deep Learning"](https://arxiv.org/pdf/2106.11342.pdf) by Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola
* :orange_book: ["Deep Learning on Graphs"](https://yaoma24.github.io/dlg_book/dlg_book.pdf) by Yao Ma and Jiliang Tang
* :orange_book: ["Physics-based Deep Learning"](https://browse.arxiv.org/pdf/2109.05237.pdf) by Nils Thuerey, Philipp Holl, Maximilian Mueller, Patrick Schnell, Felix Trost, and Kiwon Um
* :orange_book: ["Understanding Deep Learning"](https://github.com/udlbook/udlbook/releases/download/v1.15/UnderstandingDeepLearning_23_10_23_C.pdf) by Simon J. D. Prince 
* :orange_book: ["The Little Book of Deep Learning"](https://fleuret.org/public/lbdl.pdf) by François Fleuret
* :orange_book: ["Mathematical Introduction to Deep Learning: Methods, Implementations, and Theory"](https://export.arxiv.org/pdf/2310.20360) by Arnulf Jentzen, Benno Kuckuck, and Philippe von Wurstemberger
* :orange_book: ["Mathematical theory of deep learning"](https://arxiv.org/pdf/2407.18384) by Philipp Petersen, and Jakob Zech
* :orange_book: ["Theory of Deep Learning"](https://www.cs.princeton.edu/~arora/TheoryDL.pdf) by Sanjeev Arora, *et al.*
* :orange_book: ["Loss Functions and Metrics in Deep Learning"](https://arxiv.org/pdf/2307.02694) by Juan Terven, Diana M. Cordova-Esparza, Alfonso Ramirez-Pedraza, Edgar A. Chavez-Urbiola, and Julio A. Romero-Gonzalez
* :orange_book: ["Understanding Deep Learning"](https://drive.google.com/file/d/1fejSMGPIDMO4eilsIDj-7QcFsCge4vdv/view) by Chitta Ranjan
* :earth_africa: ["Deep Learning: Foundations and Concepts"](https://issuu.com/cmb321/docs/deep_learning_ebook) by Christopher M. Bishop and Hugh Bishop
* :earth_africa: ["Deep Learning for Coders with fastai and PyTorch: AI Applications Without a PhD"](https://course.fast.ai/Resources/book.html) by Jeremy Howard, and Sylvain Gugger

---
### Reinforcement learning
* :orange_book: ["Reinforcement Learning: An Introduction"](http://www.incompleteideas.net/book/RLbook2020.pdf) by Richard S. Sutton and Andrew G. Barto
* :orange_book: ["Multi-Agent Reinforcement Learning"](https://www.marl-book.com/download) by  Stefano V. Albrecht,  Filippos Christianos, and Lukas Schäfer
* :orange_book: ["Distributional Reinforcement Learning"](https://direct.mit.edu/books/book-pdf/2111075/book_9780262374026.pdf) by  Marc G. Bellemare, Will Dabney, and Mark Rowland
* :orange_book: ["Mathematical Foundations of Reinforcement Learning"](https://raw.githubusercontent.com/MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning/refs/heads/main/Book-all-in-one.pdf) by Shiyu Zhao
* :orange_book: ["Reinforcement Learning: Foundations"](https://drive.google.com/file/d/1QApF7NFEciyD3C8V5ugYcnxkg6BPutqw/view) by Shie Mannor, Yishay Mansour, and Aviv Tamar
* :orange_book: ["Reinforcement Learning: An Overview"](https://arxiv.org/pdf/2412.05265) by Kevin Murphy
* :orange_book: ["An Introduction to Deep Reinforcement Learning"](https://arxiv.org/pdf/1811.12560) by Vincent Francois-Lavet, Peter Henderson, Riashat Islam, Marc G. Bellemare, and Joelle Pineau
* :orange_book: ["The Mathematics of Reinforcement Learning"](https://www.wim.uni-mannheim.de/media/Lehrstuehle/wim/doering/RL/RL_VORLESUNG.pdf) by Leif Döring

---
### Recommender systems
* :orange_book: ["Recommender Systems"](https://arxiv.org/pdf/1202.1112.pdf) by Linyuan Lü, Matus Medo, Chi Ho Yeung, Yi-Cheng Zhang, Zi-Ke Zhang, and Tao Zhou
* :orange_book: ["Recommender Systems: A Primer"](https://arxiv.org/pdf/2302.02579) Pablo Castells, and Dietmar Jannach

---
### Anomaly detection
* :earth_africa: ["That’s weird! Anomaly detection using R"](https://otexts.com/weird/) by Rob J. Hyndman

---
### Computer vision
* :orange_book: ["Computer Vision:  Models, Learning, and Inference"](https://raw.githubusercontent.com/udlbook/cvbook/main/book.pdf) by Simon J. D. Prince
* :orange_book: ["Computer Vision: Algorithms and Applications" (1st Ed)](https://szeliski.org/Book/drafts/SzeliskiBook_20100903_draft.pdf) by Richard Szeliski

---
### Natural language processing (NLP) and large language models (LLM)
* :orange_book: ["Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition"](https://web.stanford.edu/~jurafsky/slp3/ed3bookaug20_2024.pdf) by  Dan Jurafsky and James H. Martin 
* :orange_book: ["Large Language Models"](https://arxiv.org/pdf/2307.05782.pdf) by Michael R. Douglas
* :orange_book: ["Graph Neural Networks for Natural Language Processing: A Survey"](https://arxiv.org/pdf/2106.06090.pdf) by Lingfei Wu, Yu Chen, Kai Shen, Xiaojie Guo, Hanning Gao, Shucheng Li, Jian Pei, and Bo Long
* :orange_book: ["Formal Aspects of Language Modeling"](https://arxiv.org/pdf/2311.04329.pdf) by Ryan Cotterell, Anej Svete, Clara Meister, Tianyu Liu, and Li Du
* :orange_book: ["Foundation Models for Natural Language Processing"](https://link.springer.com/content/pdf/10.1007/978-3-031-23190-2.pdf) by  Gerhard Paaß, and Sven Giesselbach
* :orange_book: ["What are embeddings"](https://raw.githubusercontent.com/veekaybee/what_are_embeddings/main/embeddings.pdf) by Vicki Boykis
* :orange_book: ["A Survey of Large Language Models"](https://arxiv.org/pdf/2303.18223.pdf) by Wayne Xin Zhao, *et al.*
* :orange_book: ["Large Language Models: A Survey"](https://arxiv.org/pdf/2402.06196) by Shervin Minaee, *et al.*
* :orange_book: ["A Comprehensive Overview of Large Language Models"](https://arxiv.org/pdf/2307.06435) by Humza Naveed, *et al.*
* :orange_book: ["A Survey on Large Language Models with some Insights on their Capabilities and Limitations"](https://arxiv.org/pdf/2501.04040) by Andrea Matarazzo, and Riccardo Torlone
* :orange_book: ["Foundations of Large Language Models"](https://arxiv.org/pdf/2501.09223) by Tong Xiao, and Jingbo Zhu
* :earth_africa: ["Text Mining with R: A Tidy Approach"](https://www.tidytextmining.com/) by Julia Silge and David Robinson
* :earth_africa: ["Natural Language Processing with Python - Analyzing Text with the Natural Language Toolkit"](https://www.nltk.org/book/) by Steven Bird, Ewan Klein, and Edward Loper

---
### Causal inference
* :orange_book: ["Causal Machine Learning: A Survey and Open Problems"](https://arxiv.org/pdf/2206.15475.pdf) by Jean Kaddour, Aengus Lynch, Qi Liu, Matt J. Kusner, and Ricardo Silva
* :orange_book: ["Recent Developments in Causal Inference and Machine Learning"](https://www.annualreviews.org/doi/pdf/10.1146/annurev-soc-030420-015345) by Jennie E. Brand, Xiang Zhou, and Yu Xie
* :orange_book: ["A First Course in Causal Inference"](https://arxiv.org/pdf/2305.18793.pdf) by Peng Ding
* :orange_book: ["Causal Factor Investing"](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9AFE270D7099B787B8FD4F4CBADE0C6E/9781009397292AR.pdf/causal-factor-investing.pdf) by Marcos M. López de Prado
* :orange_book: ["Survey and Evaluation of Causal Discovery Methods for Time Series"](https://www.jair.org/index.php/jair/article/view/13428/26917) by Charles K. Assaad, Emilie Devijver, and Eric Gaussier
* :orange_book: ["Applied Causal Inference Powered by ML and AI"](https://arxiv.org/pdf/2403.02467v1.pdf) by Victor Chernozhukov, Christian Hansen, Nathan Kallus, Martin Spindler, and Vasilis Syrgkanis
* :orange_book: ["Causal Inference: A Statistical Learning Approach"](https://web.stanford.edu/~swager/causal_inf_book.pdf) by Stefan Wager
* :earth_africa: ["Applied Causal Inference"](https://appliedcausalinference.github.io/aci_book/) by Uday Kamath, Kenneth Graham, and Mitchell Naylor
* :earth_africa: ["Causal Inference for The Brave and True"](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) by Matheus Facure Alves

---
### Conformal prediction
* :orange_book: ["A Tutorial on Conformal Prediction"](https://arxiv.org/pdf/0706.3188.pdf) by Glenn Shafer and Vladimir Vovk
* :orange_book: ["Conformal Prediction: a Unified Review of Theory and New Challenges"](https://arxiv.org/pdf/2005.07972.pdf) by Matteo Fontana, Gianluca Zeni and Simone Vantini
* :orange_book: ["A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"](https://arxiv.org/pdf/2107.07511.pdf) by Anastasios N. Angelopoulos and Stephen Bates
* :orange_book: ["Theoretical Foundations of Conformal Prediction"](https://arxiv.org/pdf/2411.11824) by Anastasios N. Angelopoulos, Rina Foygel Barber, and Stephen Bates
* :orange_book: ["Machine Learning Learning Beyond Point Predictions: Uncertainty Quantification"](https://rafaelizbicki.com/UQ4ML.pdf) by Rafael Izbicki

---
### Time series: Forecasting
* :earth_africa: ["Forecasting: Principles and Practice"](https://otexts.com/fpp3/) by Rob J Hyndman and George Athanasopoulos
* :orange_book: ["Forecasting: theory and practice"](https://arxiv.org/pdf/2012.03854.pdf) by Fotios Petropoulos *et al.*
* :earth_africa: ["Forecasting: theory and practice" (Online version)](https://forecasting-encyclopedia.com/) Editors: Fotios Petropoulos, Yanfei Kang, and  Feng Li
* :orange_book: ["Forecast Evaluation for Data Scientists: Common Pitfalls and Best Practices"](https://arxiv.org/pdf/2203.10716.pdf) by Hansika Hewamalagea, Klaus Ackermannb, and Christoph Bergmeir
* :orange_book: ["A Comprehensive Survey of Regression Based Loss Functions for Time Series Forecasting"](https://arxiv.org/pdf/2211.02989.pdf) by Aryan Jadon, Avinash Patil and Shruti Jadon
* :orange_book: ["Time Series Analysis"](https://batch.libretexts.org/print/Letter/Finished/stats-826/Full.pdf) by Alexander Aue
* :orange_book: ["Time Series for Macroeconomics and Finance"](https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5ed92dcb7665261af1aa23f2/1591291342389/time_series_book.pdf) by John H. Cochrane
* :earth_africa: ["Demand Forecasting for Executives and Professionals"](https://dfep.netlify.app/) by Stephan Kolassa, Bahman Rostami-Tabar, and Enno Siemsen

---
