import random
import time

def wait_a_sec():
  sleep_time = random.random()
  time.sleep(sleep_time)

def print_config(args):
  config = vars(args) # same as args just in dict format
  print("---\nConfiguration\n---")
  col_width = max([len(x) for x in config.keys()]) + 2
  template = "  {:>%d} {}" % col_width
  for k in sorted(config.keys()):
    v = config[k]
    print(template.format("{}:".format(k), v))
  print("---")


def add_to_qri(args):
  print("...adding to qri")