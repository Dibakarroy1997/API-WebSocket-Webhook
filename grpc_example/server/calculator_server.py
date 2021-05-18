import os
from concurrent import futures
from time import sleep

import grpc
from grpc_reflection.v1alpha import reflection

import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorService):
    def Sum(self, request, context):
        return calculator_pb2.Number(value=request.x + request.y)

    def PrimeNumberGenerator(self, request, context):
        for num in range(2, request.value):
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                sleep(1)
                yield calculator_pb2.Number(value=num)

    def FindMaximum(self, request_iterator, context):
        maxNumber = 0
        for number in request_iterator:
            if number.value > maxNumber:
                yield calculator_pb2.Number(value=number.value)
                maxNumber = number.value

    def ComputerAverage(self, request_iterator, context):
        numbers = list()
        for number in request_iterator:
            numbers.append(number.value)
        return calculator_pb2.Float(value=sum(numbers) / len(numbers))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(Calculator(), server)
    server.add_insecure_port("[::]:50051")
    SERVICE_NAMES = (calculator_pb2.DESCRIPTOR.services_by_name['CalculatorService'].full_name, reflection.SERVICE_NAME)
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    # os.environ["GRPC_VERBOSITY"] = "DEBUG"
    # os.environ["GRPC_TRACE"] = "http"
    print('Starting server. Listening on port 50051...')
    serve()
