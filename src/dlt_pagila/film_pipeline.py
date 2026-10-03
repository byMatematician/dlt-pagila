import dlt
from dlt.sources.sql_database import sql_database


def main():
    # Source: which database and which tables to read
    source = sql_database(
        credentials="postgresql://bymatchi@localhost:5432/pagila",
        table_names=["film", "actor", "film_actor", "customer", "rental"],
    )

    # Pipeline: where the data goes
    pipeline = dlt.pipeline(
        pipeline_name="pagila_gcs",
        destination=dlt.destinations.filesystem(bucket_url="gs://kutbi-pagila-raw"),
        dataset_name="pagila_raw",
    )

    # Run: full load, written as Parquet
    load_info = pipeline.run(
        source,
        loader_file_format="parquet",
        write_disposition="replace",
    )
    print(load_info)


if __name__ == "__main__":
    main()