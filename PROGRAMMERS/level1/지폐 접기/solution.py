def solution(wallet, bill):
    answer = 0
    wallet.sort()
    while 1:
        bill.sort()
        if bill[1] > wallet[1] or bill[0] > wallet[0]:
            bill[1] //= 2
            answer += 1

        else:
            break

    return answer
