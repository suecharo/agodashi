# dashi

<!-- [![pytest](https://github.com/suecharo/dashi/workflows/pytest/badge.svg)](https://github.com/suecharo/dashi/actions?query=workflow%3Apytest)
[![flake8](https://github.com/suecharo/dashi/workflows/flake8/badge.svg)](https://github.com/suecharo/dashi/actions?query=workflow%3Aflake8)
[![isort](https://github.com/suecharo/dashi/workflows/isort/badge.svg)](https://github.com/suecharo/dashi/actions?query=workflow%3Aisort)
[![mypy](https://github.com/suecharo/dashi/workflows/mypy/badge.svg)](https://github.com/suecharo/dashi/actions?query=workflow%3Amypy) -->
[![Apache License](https://img.shields.io/badge/license-Apache%202.0-orange.svg?style=flat&color=important)](http://www.apache.org/licenses/LICENSE-2.0)

[dashi API specification - Swagger UI](https://suecharo.github.io/dashi-swagger-ui/)

## Install and Run

Dashi supports Python 3.6 or newer.

```bash
$ pip3 install dashi
$ dashi
```

### Docker

We also expect to launch using Docker.

```bash
# Launch
$ docker-compose up -d

# Launch confirmation
$ docker-compose logs
```

## Development

The development environment can be started as follows.

```bash
$ docker-compose -f docker-compose.dev.yml up -d --build
$ docker-compose -f docker-compose.dev.yml exec app bash
```

We use [flake8](https://pypi.org/project/flake8/), [isort](https://github.com/timothycrosley/isort), and [mypy](http://mypy-lang.org) as linters.

```bash
$ bash ./tests/lint_and_style_check/flake8.sh
$ bash ./tests/lint_and_style_check/isort.sh
$ bash ./tests/lint_and_style_check/mypy.sh
```

We also use [pytest](https://docs.pytest.org/en/latest/) as a test tool.

```bash
$ pytest .
```

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](https://github.com/suecharo/dashi/blob/master/LICENSE).

- The Developer and Maintainer: [@suecharo](https://github.com/suecharo)
