from snowflake_id import SnowflakeIDGenerator

TIMESTAMP = 1735689600


def test_it_should_return_snowflake_id() -> None:
    generate_snowflake_id = SnowflakeIDGenerator(
        node_id=1,
        timestamp_generator=lambda: TIMESTAMP,
    )

    snowflake_id = generate_snowflake_id()

    assert snowflake_id == (TIMESTAMP << 32 | 0x0001 << 16 | 0x0001).to_bytes(
        length=8, byteorder="big"
    )


def test_sequence_number_should_increase_in_same_second() -> None:
    generate_snowflake_id = SnowflakeIDGenerator(
        node_id=1,
        timestamp_generator=lambda: TIMESTAMP,
    )

    generate_snowflake_id()
    snowflake_id = generate_snowflake_id()

    assert snowflake_id == (TIMESTAMP << 32 | 0x0001 << 16 | 0x0002).to_bytes(
        length=8, byteorder="big"
    )
