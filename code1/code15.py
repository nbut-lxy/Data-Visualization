import turtle
import time
if __name__=="__main__":
	t = turtle.Pen();
	t.shape('turtle');
	t.fillcolor('orange');
	t.pencolor('blue');
	t.begin_fill();
	t.fd(100);
	t.left(72);
	t.fd(100);
	t.left(72);
	t.fd(100);
	t.left(72);
	t.fd(100);
	t.left(72);
	t.fd(100);
	t.left(72);
	t.end_fill();
	time.sleep(3)