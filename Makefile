all :
	nohup python apiByt.py 8080 &
clean : 
	rm *.pyc
	rm  clases/*.pyc
