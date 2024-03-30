from kfp import dsl
from kfp.v2.dsl import ContainerSpec

# コンポーネントを定義
@dsl.container_component
def add_component() -> ContainerSpec:
    return ContainerSpec(
        image='gcr.io/keiba-hacke/add_docker',
        command=["python3", "add.py", "--x", "1", "--y", "2"]
    )