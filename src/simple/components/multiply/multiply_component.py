from kfp import dsl
from kfp.v2.dsl import ContainerSpec

# コンポーネントを定義
@dsl.container_component
def multiply_component() -> ContainerSpec:
    return ContainerSpec(
        image='gcr.io/keiba-hacke/multiply_docker',
        command=["python3", "multiply.py", "--z", "3", "--w", "3"]
    )