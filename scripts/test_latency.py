import time
import os
from fastembed import TextEmbedding

print("Initializing TextEmbedding with default threads...")
t0 = time.perf_counter()
model_default = TextEmbedding("BAAI/bge-small-en-v1.5")
print(f"Init default took {(time.perf_counter() - t0)*1000:.1f}ms")

# Warm up
list(model_default.embed(["hello world"]))

print("\nBenchmarking default:")
for i in range(10):
    t0 = time.perf_counter()
    list(model_default.embed(["hello world"]))
    print(f"  Run {i}: {(time.perf_counter() - t0)*1000:.2f}ms")

print("\nInitializing TextEmbedding with threads=1...")
t0 = time.perf_counter()
model_t1 = TextEmbedding("BAAI/bge-small-en-v1.5", threads=1)
print(f"Init threads=1 took {(time.perf_counter() - t0)*1000:.1f}ms")

# Warm up
list(model_t1.embed(["hello world"]))

print("\nBenchmarking threads=1:")
for i in range(10):
    t0 = time.perf_counter()
    list(model_t1.embed(["hello world"]))
    print(f"  Run {i}: {(time.perf_counter() - t0)*1000:.2f}ms")
