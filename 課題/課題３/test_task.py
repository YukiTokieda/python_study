import unittest
import task

class TestTask(unittest.TestCase):

# 日付
  def test_group_func1(self):
    df =[]
    task.group_func(df, ['A'], '2020')

  def test_group_func2(self):
    df =[]
    task.group_func(df, ["A"], '2020-02')

  def test_group_func3(self):
    df =[]
    task.group_func(df, ["A"],'2020-03-01')

  def test_group_func4(self):
    df =[]
    task.group_func(df, ["A"],'202')

# group
  def test_group_func5(self):
    df =[]
    task.group_func(df, ["B"], '2020')

  def test_group_func6(self):
    df =[]
    task.group_func(df, ["X"], '2020')

  def test_group_func7(self):
    df =[]
    task.group_func(df, ["Y"], '2020')

  def test_group_func8(self):
    df =[]
    task.group_func(df, ["A","X"], '2020')

  def test_group_func9(self):
    df =[]
    task.group_func(df, ["B","Y"], '2020')

  def test_group_func10(self):
    df =[]
    task.group_func(df, [], '2020')

  def test_group_func12(self):
    df =[]
    task.group_func(df, ["C"], '2020')

  def test_group_func13(self):
    df =[]
    task.group_func(df, ['A',"B","Y"], '2020')

  def test_group_func14(self):
    df =[]
    task.group_func(df, ['A',"B"], '2020')

  def test_group_func15(self):
    df =[]
    task.group_func(df, ["X","Y"], '2020')


