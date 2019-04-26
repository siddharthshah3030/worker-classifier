# Profession Classifier
a simplle image classifier based on ImageAI 

<br>
Trying to classify work and professions of people  

# Features!

  - Classifies professions of people based on images
  
You can modify the same for many other similar applications 
### Tech

[ImageAI](https://github.com/OlafenwaMoses/ImageAI) state of the art computer vision capabilities
 Image prediction model - Resnet ( as of now ) 
### Dataset 
IdenProf (Identifiable Professionals) is a dataset that contains 11,000 pictures of 10 different professionals that humans can see and recognize their jobs by their mode of dressing. The classes of professionals whose pictures are in this dataset are as below:

· Chef
· Doctor
· Engineer
· Farmer
· Firefighter
· Judge
· Mechanic
· Pilot
· Police
· Waiter

This dataset is split into 9000 (900 pictures for each profession) pictures to train the artificial intelligence model and 2000 (200 pictures for each profession) 



### <b>>>> Prediction Results</b> <br><br>
  <img src="test-images/1.jpg" />
<pre>
chef  :  99.90828037261963
waiter  :  0.0905417778994888
doctor  :  0.0011116820132883731
</pre>

<hr>
<br>
<img src="test-images/2.jpg" />
<pre>
firefighter  :  80.1691472530365
police  :  19.79282945394516
engineer  :  0.03719799569807947
</pre>

<hr>
<br>

<img src="test-images/3.jpg" />
<pre>
farmer  :  99.93320107460022
police  :  0.06526767974719405
firefighter  :  0.0014684919733554125
</pre>

<hr>

<br>

<img src="test-images/5.jpg" />
<pre>
waiter  :  99.99997615814209
chef  :  1.568847380895022e-05
judge  :  1.0255866556008186e-05
</pre>

<hr>

<br>

<img src="test-images/7.jpeg" />
<pre>
farmer  :  100.0
waiter  :  1.6071012576279742e-09
police  :  1.273151375991155e-09
</pre>

<hr>


<br>

<img src="test-images/10.jpg" />
<pre>
police  :  96.9819724559784
pilot  :  2.988756448030472
engineer  :  0.029250176157802343
</pre>

### Development

Simply:
```sh
$ python main.py
```






### Todos

 - Increase efficiency
 - Perform tests on other datasets

License
----

MIT




