# ActivityPub-Scraping-Research

## What is this projects Goal

* Index an entire activitypub profile into a database
* Write indexed activitypub profile to another activity account
* Index and republish other microblog and blog formats such as twitter, gab, truth social etc.

## Index entire ActivityPub Profile

* Functions
  * CHECK Index all posts from specific user
  * Get all followers of specific user
  * Get all users a user follows
  * CHECK Get profile description
    * Get number of posts from specific user
  * Get likes
  * Get pinned posts
  * Get Replies
* We need some test servers to work with
  * 
* We need example users who are they
  * [Joanna Masel (@JoannaMasel@fediscience.org) - FediScience.org](https://fediscience.org/@JoannaMasel)
  * [Pleroma/Soykaf](https://pleroma.soykaf.com/users/lain)
  * [Eugen 💀 (@Gargron@mastodon.social) - Mastodon](https://mastodon.social/@Gargron)

## Requirements

* python3
* pip
* nodejs
* npm / yarn

## Install

``` bash
npm install -g ts-node typescript '@types/node'
npm i --save-dev @types/node

npx ts-node typescript-file.ts

ts-node-esm typescript-file.ts
```

## Instructions

TODO

## TODO Research

* [MastoVue | Mastodon Timeline Viewer](https://mastovue.glitch.me/#/)
* Get a working example that pull's data
  * [Playing with public data - Mastodon documentation](https://docs.joinmastodon.org/client/public/)
  * Megalodon
    * [GitHub - h3poteto/megalodon: Mastodon, Pleroma and Misskey API client library for node.js and browser](https://github.com/h3poteto/megalodon)
    * [megalodon](https://h3poteto.github.io/megalodon/)
    * [h3poteto/megalodon-rs: Mastodon and Pleroma API client library for Rust](https://github.com/h3poteto/megalodon-rs)
* AWESOME LISTS
  * [tleb/awesome-mastodon: Curated list of awesome Mastodon-related stuff!](https://github.com/tleb/awesome-mastodon)
* Other
  * [Trunk for the Fediverse](https://communitywiki.org/trunk)
  * [Access Token Generator for Mastodon API](https://takahashim.github.io/mastodon-access-token/?code=uNiIGtL4L4AxsDHgk8XBSPTQDaypFOB8YNB_7J_eT0M)
* API Documentation
  * [Fetching ActivityPub Feeds - Gokberk Yaltirakli](https://www.gkbrk.com/2018/06/fetching-activitypub-feeds/)
  * [Misskey API](https://misskey.io/api-doc)
  * [Getting started with the API - Mastodon documentation](https://docs.joinmastodon.org/client/intro/)
  * [Pleroma API - Pleroma Documentation](https://docs-develop.pleroma.social/backend/development/API/pleroma_api/)
  * [Eugen 💀: "Summary of the #Pleroma API ch…" - Mastodon](https://mastodon.social/@Gargron/101489729849684852)
* Exporting your Data
  * [Moving or leaving accounts - Mastodon documentation](https://docs.joinmastodon.org/user/moving/)
    * Full export possible if you request it
  * [Settings - Pleroma Documentation](https://docs-develop.pleroma.social/frontend/user_guide/settings/#data-importexport)
    * Full export possible but not import just like Mastadon
  * Misskey does not natively support this feature
    * [GitHub - coke12103/misskey-follow-import: フォローインポートが正常に機能しないインスタンスの住民に向けて。](https://github.com/coke12103/misskey-follow-import)
* Other Tooling
  * [Misskey Tools](https://misskey.tools/apps/miss-hai/ranking)
