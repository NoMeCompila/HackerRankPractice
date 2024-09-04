"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
sample
input -> 2 3 6 6 5
output -> 5
"""
if __name__ == "__main__":
    def runner_up_score(arr: list) -> None:
        order_num = sorted(arr)
        result = list(set(order_num))
        print(result[-2])

    runner_up_score([2, 3, 6, 6, 5])