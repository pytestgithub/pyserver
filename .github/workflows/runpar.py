jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: ["linux", "darwin"]
    steps:
      - name: Build
        run: |
          function build() {
            if [[ "${{ matrix.os }}-${2}" == "darwin-386" ]]; then
              exit 0
            fi
            GOOS="${{ matrix.os }}" GOARCH="${2}" \
              go build -o "main-${{ matrix.os }}-${2}" ./...
          }
          export -f build
          parallel -j0 build ::: "amd64" "386"
