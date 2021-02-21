# 512 Kb

## Redis AOF, 512Kb (with output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                 461.80 secs
Data transferred:             250.01 MB
Response time:                 22.41 secs
Transaction rate:               1.08 trans/sec
Throughput:                     0.54 MB/sec
Concurrency:                   24.27
Successful transactions:         500
Failed transactions:               0
Longest transaction:           27.66
Shortest transaction:           9.97


## Redis RDB, save 1 1, 512Kb (with output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                 463.08 secs
Data transferred:             250.01 MB
Response time:                 22.51 secs
Transaction rate:               1.08 trans/sec
Throughput:                     0.54 MB/sec
Concurrency:                   24.31
Successful transactions:         500
Failed transactions:               0
Longest transaction:           27.21
Shortest transaction:          13.06


## Redis RDB, save 100 1, 512Kb (with output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege...                                                                                                                                            done.

Transactions:                    442 hits
Availability:                  88.40 %
Elapsed time:                 445.46 secs
Data transferred:             137.01 MB
Response time:                 22.24 secs
Transaction rate:               0.99 trans/sec
Throughput:                     0.31 MB/sec
Concurrency:                   22.06
Successful transactions:         442
Failed transactions:              58
Longest transaction:           29.16
Shortest transaction:           5.81


## Redis RDB, save 100 1, 512Kb (w/o output)
### Trying to check hypothesis that the bottleneck is in transferred data (no big changes)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege...                                                                                                                                         done.

Transactions:                    495 hits
Availability:                  99.00 %
Elapsed time:                 475.63 secs
Data transferred:               0.03 MB
Response time:                 23.08 secs
Transaction rate:               1.04 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   24.02
Successful transactions:         495
Failed transactions:               5
Longest transaction:           29.86
Shortest transaction:          11.95


## Redis RDB, no saving, 512Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    476 hits
Availability:                  95.20 %
Elapsed time:                 478.11 secs
Data transferred:               0.02 MB
Response time:                 23.71 secs
Transaction rate:               1.00 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   23.61
Successful transactions:         476
Failed transactions:              24
Longest transaction:           29.51
Shortest transaction:          17.40


## Beanstalk, 512Kb (w/o output)
Doesn't work


# 63 Kb

## Beanstalk, with saving, 63Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  69.30 secs
Data transferred:               0.03 MB
Response time:                  2.85 secs
Transaction rate:               7.22 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   20.57
Successful transactions:         500
Failed transactions:               0
Longest transaction:            6.21
Shortest transaction:           0.25


## Beanstalk, w/o saving, 63Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  56.13 secs
Data transferred:               0.03 MB
Response time:                  2.23 secs
Transaction rate:               8.91 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   19.86
Successful transactions:         500
Failed transactions:               0
Longest transaction:            3.43
Shortest transaction:           0.20


## Redis, w/o saving, 63Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  55.78 secs
Data transferred:               0.03 MB
Response time:                  2.19 secs
Transaction rate:               8.96 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   19.67
Successful transactions:         500
Failed transactions:               0
Longest transaction:            3.49
Shortest transaction:           0.05


## Redis, save 1 1, 63Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  56.83 secs
Data transferred:               0.03 MB
Response time:                  2.22 secs
Transaction rate:               8.80 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   19.55
Successful transactions:         500
Failed transactions:               0
Longest transaction:            3.27
Shortest transaction:           0.05
 

## Redis, AOF, 63Kb (w/o output)

docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000
Creating 10-queues_siege_run ... done
** SIEGE 3.0.5
** Preparing 25 concurrent users for battle.
The server is now under siege..      done.

Transactions:                    500 hits
Availability:                 100.00 %
Elapsed time:                  60.62 secs
Data transferred:               0.03 MB
Response time:                  2.46 secs
Transaction rate:               8.25 trans/sec
Throughput:                     0.00 MB/sec
Concurrency:                   20.29
Successful transactions:         500
Failed transactions:               0
Longest transaction:            4.29
Shortest transaction:           0.05
