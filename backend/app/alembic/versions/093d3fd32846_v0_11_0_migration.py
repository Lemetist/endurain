"""v0.11.0 migration

Revision ID: 093d3fd32846
Revises: cde44b1247dc
Create Date: 2025-05-13 23:01:59.971649

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "093d3fd32846"
down_revision: Union[str, None] = "cde44b1247dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Set all Strava-related fields to NULL for every entry in users_integrations
    op.execute(
        "UPDATE users_integrations SET strava_client_id = NULL, strava_client_secret = NULL, "
        "strava_state = NULL, strava_token = NULL, strava_refresh_token = NULL, "
        "strava_token_expires_at = NULL, garminconnect_oauth1 = NULL, garminconnect_oauth2 = NULL"
    )
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users_integrations",
        "strava_client_id",
        existing_type=sa.INTEGER(),
        type_=sa.String(length=512),
        comment="Strava client ID encrypted at rest with Fernet key",
        existing_comment="Strava client ID",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_client_secret",
        existing_type=sa.VARCHAR(length=250),
        type_=sa.String(length=512),
        comment="Strava client secret encrypted at rest with Fernet key",
        existing_comment="Strava client secret",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_token",
        existing_type=sa.VARCHAR(length=250),
        type_=sa.String(length=512),
        comment="Strava token after link process encrypted at rest with Fernet key",
        existing_comment="Strava token after link process",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_refresh_token",
        existing_type=sa.VARCHAR(length=250),
        type_=sa.String(length=512),
        comment="Strava refresh token after link process encrypted at rest with Fernet key",
        existing_comment="Strava refresh token after link process",
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users_integrations",
        "strava_refresh_token",
        existing_type=sa.VARCHAR(length=250),
        comment="Strava refresh token after link process",
        existing_comment="Strava refresh token after link process encrypted at rest with Fernet key",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_token",
        existing_type=sa.VARCHAR(length=250),
        comment="Strava token after link process",
        existing_comment="Strava token after link process encrypted at rest with Fernet key",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_client_secret",
        existing_type=sa.VARCHAR(length=250),
        comment="Strava client secret",
        existing_comment="Strava client secret encrypted at rest with Fernet key",
        existing_nullable=True,
    )
    op.alter_column(
        "users_integrations",
        "strava_client_id",
        existing_type=sa.String(length=250),
        type_=sa.INTEGER(),
        comment="Strava client ID",
        existing_comment="Strava client ID encrypted at rest with Fernet key",
        existing_nullable=True,
    )
    # ### end Alembic commands ###
