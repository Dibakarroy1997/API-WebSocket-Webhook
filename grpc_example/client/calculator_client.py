from __future__ import print_function

import logging
from time import sleep

import grpc

import calculator_pb2
import calculator_pb2_grpc


def generate_numbers():
    numbers = [65, 3, 7, 1, 78, 33, 55, 88, 44, 76, 101]
    for number in numbers:
        print(f"Sending {number} to the server from client...")
        yield calculator_pb2.Number(value=number)
        sleep(1)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorServiceStub(channel)

        print(f"\n{'*' * 20} Sum {'*' * 20}")
        response = stub.Sum(calculator_pb2.SumRequest(x=1, y=2))
        print(f"Sum Value received from server: {response.value}")

        print(f"\n{'*' * 20} Prime Number Generator {'*' * 20}")
        responses = stub.PrimeNumberGenerator(calculator_pb2.Number(value=10))
        for response in responses:
            print(f"Next prime number received from server: {response.value}")

        print(f"\n{'*' * 20} Find Maximum Number {'*' * 20}")
        responses = stub.FindMaximum(generate_numbers())
        for response in responses:
            print(f"Got new max number from server: {response.value}")

        print(f"\n{'*' * 20} Find Average of numbers {'*' * 20}")
        response = stub.ComputerAverage(generate_numbers())
        print(f"Average number received from server: {response.value}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
