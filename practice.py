# """practice.py
# Simple utility to find the maximum (largest) and minimum (smallest) elements
# in a list of numbers entered by the user.

# Usage:
#  - Enter numbers separated by spaces when prompted, or press Enter to use
#    a default example list.
# """

# from typing import List, Tuple


# def get_numbers_from_input(prompt: str = "Enter numbers separated by spaces (empty for example list): ") -> List[float]:
#     s = input(prompt).strip()
#     if not s:
#         # example default list
#         return [3, 1, 4, 1, 5, 9]
#     parts = s.split()
#     nums: List[float] = []
#     for p in parts:
#         try:
#             if "." in p:
#                 nums.append(float(p))
#             else:
#                 nums.append(int(p))
#         except ValueError:
#             raise ValueError(f"Invalid number: {p}")
#     return nums


# def manual_min_max(nums: List[float]) -> Tuple[float, float]:
#     if not nums:
#         raise ValueError("Empty list")
#     smallest = largest = nums[0]
#     for n in nums[1:]:
#         if n < smallest:
#             smallest = n
#         if n > largest:
#             largest = n
#     return smallest, largest


# def main() -> None:
#     try:
#         nums = get_numbers_from_input()
#     except ValueError as e:
#         print(e)
#         return

#     print("Numbers:", nums)

#     # Using built-in functions
#     print("Built-in min:", min(nums))
#     print("Built-in max:", max(nums))

#     # Using manual method
#     small, large = manual_min_max(nums)
#     print("Manual smallest:", small)
#     print("Manual largest:", large)


# if __name__ == "__main__":
#     main()



# # Example output:
# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings

# # create your views here.
# def send_request(request):
#     if request.method == 'POST':
#         to = request.POST.get('to')
#         subject = request.POST.get('subject')
#         print(to, subject)
#         return render(request, 'css/send.html', {'to': to, 'subject': subject})
#     else:
#         return render(request, 'css/send.html') 
    

#     # email settings
#     email_host = 'smtp.gmail.com'   
#     email_port = 587
#     email_use_tls = True
#     email_host_user = 'narayan@yahoo.com'
#     email_host_password = 'Espresso@50' 
#     email_backend = 'django.core.mail.backends.smtp.EmailBackend'

# def send_email(request):
#     if request.method == 'POST':
#         to = request.POST.get('to')
#         subject = request.POST.get('subject')
#         message = 'This is a test email sent from Django.'
#         return render(request, 'css/sent.html', {'to': to})
#     else:
#         return render(request, 'css/send.html')
    
#     send_mail((password=0909)
#               9090
#               while
#                 subject,
#                 message,

#                 from_email=
#                 settings.EMAIL_HOST_USER,
#                 recipient_list=[to],
#                 fail_silently=False

#         example of multithreading in python
import threading
import time
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Finished printing numbers and letters.")#         )  