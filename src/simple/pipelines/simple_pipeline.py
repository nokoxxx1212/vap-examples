from google.cloud import aiplatform
from kfp import dsl
from kfp.v2 import compiler
from dotenv import load_dotenv
import os
from src.simple.components.add.add_component import add_component
from src.simple.components.multiply.multiply_component import multiply_component


# パイプラインを定義
@dsl.pipeline(
    name='simple-pipeline',
    description='A pipeline to add and multiply numbers'
)
def simple_pipeline():
    # コンポーネントのインスタンスを作成
    add_task = add_component()
    multiply_task = multiply_component()
    multiply_task.after(add_task)

# パイプラインを実行
def run_pipeline(project: str, location: str, pipeline_root: str):
    # Vertex AI clientを初期化
    aiplatform.init(project=project, location=location)

    # パイプラインを実行
    job = aiplatform.PipelineJob(
        display_name='simple-pipeline',
        template_path='simple_pipeline_job.json',
        pipeline_root=pipeline_root,
    )
    job.run()

if __name__ == '__main__':
    # パイプラインを実行するためのパラメータ
    env_path = f".env.{os.getenv('APP_ENV', 'dev')}"
    load_dotenv(dotenv_path=env_path)
    PROJECT_ID = os.getenv('PROJECT_ID')
    LOCATION = os.getenv('LOCATION')
    PIPELINE_ROOT = os.getenv('PIPELINE_ROOT')

    # パイプラインをコンパイル
    compiler.Compiler().compile(
        pipeline_func=simple_pipeline,
        package_path='simple_pipeline_job.json'
    )

    # パイプラインを実行
    run_pipeline(PROJECT_ID, LOCATION, PIPELINE_ROOT)