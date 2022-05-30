# plank-test

This is a django application developed as a technical interview for the plank company.

## How to start
Let's assume that you have `virtualenv` installed on your machine (if not, you can install it following [these](https://virtualenv.pypa.io/en/latest/) steps)

```bash
virtualenv plank
source plank/bin/activate
make install
./manage.py makemigrations satellites
make migrate
make run
```

and that's it, you already have your django app running. Time to try it! You have a [swagger-ui](http://127.0.0.1:8000/) to test APIs.


### About the geo position API
I used the [geopy](https://geopy.readthedocs.io/en/stable/#module-geopy.distance) library, which provide a function to calculate the **distance between** two geographical points, i.e, (latitude, longitude). The solution is clearly not the optimal, but I consider that it's sufficient for this context. The solution iterate all the points where the satellites are located and calculates the distance to the received point as parameters, if distance is less, the satellite is added to the result; otherwise it's discarded.
