FROM golang:1.13 AS build
WORKDIR /src
COPY ["go.mod", "go.sum", "./"]
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -mod=readonly

# TODO: security issue with mount
# FROM gcr.io/distroless/static:nonroot
FROM alpine:3.11
COPY --from=build /src/nginx-subrequest-auth-jwt /
ENTRYPOINT ["/nginx-subrequest-auth-jwt"]
# ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]
