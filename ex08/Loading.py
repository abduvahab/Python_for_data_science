import sys, time

def ft_tqdm(iterable, desc="progressing:",bar_len=50)->None:
    total =len(iterable)
    progress_format = f"{desc} [{{:<{bar_len}}}] {{}}/{{}} - {{:.2%}}\r"
    for i, item in enumerate(iterable,1):
        progress = i/total
        percentage = int(bar_len * progress)
        progress_str = "=" * percentage + ">"
        
        sys.stdout.write(progress_format.format(progress_str, i, total, progress))
        sys.stdout.flush()
        yield item
    # sys.stdout.write("\n")
    pass


# def main():
#     data = range(10)
#     for _ in ft_tqdm(data):
#         time.sleep(0.1)
#     print()    
# if (__name__ == "__main__"):
#     main()


