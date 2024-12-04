if __name__ == '__main__':
    c='Hello'

try:
    import numpy as np
except ImportError:
    raise ImportError("Warning: Error importing numpy. Check the module is installed on your system")

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Warning: Error importing Matplotlib. Check the module is installed on your system")

except Exception as e:
    print(f"Warning: {e}")

plt.savefig('test.png')
plt.close()

#else:
    #raise ValueError(f"Unsupported distribution: {e}")