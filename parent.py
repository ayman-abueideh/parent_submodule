from child_submodule.child import child_submodule
def parent_submodule():
    print('hello world from parent')
    child_submodule()

parent_submodule()
