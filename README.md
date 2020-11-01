# Reddit Database

## About
PostgreSQL database to host Reddit data.

## E/R Diagram

![Reddit Database Screenshot 1](screenshot_1.png)

## Database Schema

![Reddit Database Screenshot 2](screenshot_2.png)

## Importing

When doing the importing I used the following:

- **Computer:** Lenovo X1 Carbon, RAM: 15,4 GiB, CPU: Intel® Core™ i7-8550U CPU @ 1.80GHz × 8, Graphics: Intel® UHD Graphics 620 (Kabylake GT2), OS-type: 64-bitars, SSD: 256,1 GB, OS: Ubuntu 19.10 
- **Programming Language:** Python 3.7 (psycopg2 connector module used)
- **Database Client:** Postbird
- **Dataset**: JSON file “RC_2011-07”

## Results

### Import with constraints

![Reddit Database Screenshot 3](screenshot_3.png)<br />

**Total amount of time for import:** 6:42:35.211313

### Import without constraints

![Reddit Database Screenshot 4](screenshot_4.png)<br />

**Total amount of time for import:** 5:35:23.910182

## License

The license is MIT. You are free to do whatever you want with it.
