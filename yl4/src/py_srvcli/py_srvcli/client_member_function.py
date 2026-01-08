import sys

from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = int(a)
        self.req.b = int(b)
        self.future = self.cli.call_async(self.req)
        return self.future


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print('Usage: ros2 run py_srvcli client A B')
        return 1

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(sys.argv[1], sys.argv[2])

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if future.done():
            try:
                response = future.result()
            except Exception as e:
                minimal_client.get_logger().info(f'Service call failed {e!r}')
            else:
                minimal_client.get_logger().info(
                    f'Result of add_two_ints: for {minimal_client.req.a} + {minimal_client.req.b} = {response.sum}'
                )
            break

    minimal_client.destroy_node()
    rclpy.shutdown()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
