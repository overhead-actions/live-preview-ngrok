# live-preview

### Authors

 - Arthur Diniz <arthurbdiniz@gmail.com>
 - Victor Moura <victor_cmoura@hotmail.com>

 ```yml
 name: Live Preview

on: pull_request

jobs:
  live-preview:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Start services
        run: docker-compose up -d

      - name: Start tunnel
        uses: overhead-actions/live-preview@readme-authors
        with:
          protocol: http
          port: 4000
          ngrok_authtoken: ${{ secrets.NGROK_AUTHTOKEN }}

      - name: Get URL
        id: vars
        run: echo "::set-output name=url::$(curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url)"

      - name: Comment PR
        uses: unsplash/comment-on-pr@v1.3.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          msg: 'Live preview URL: ${{ steps.vars.outputs.url }}'
          check_for_duplicate_msg: false

      - name: Wait
        run: sleep 300
```

## License

MIT Licensed. See [LICENSE](https://github.com/overhead-actions/live-preview/blob/master/LICENSE) for full details.