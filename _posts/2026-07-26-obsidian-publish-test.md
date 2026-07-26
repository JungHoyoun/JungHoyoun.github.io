---
published: true
title: Obsidian 블로그 발행 테스트
date: 2026-07-26
description: Obsidian Slip-box에서 Jekyll Chirpy로 이어지는 비공개 발행 경로를 검증한다.
categories:
  - PKM
tags:
  - Obsidian
  - Blog
permalink: /notes/obsidian-publish-test/
---

# Obsidian 블로그 발행 테스트

이 글은 `0. Slip-box/`에서 GitHub Pages까지 이어지는 발행 경로를 검증하기 위한 테스트 글이다.

## 검증할 것

- 한글 본문이 깨지지 않는다.
- **굵은 글씨**와 `inline code`가 유지된다.
- 코드 블록이 올바르게 표시된다.
- `published: true`로 전환하면 실제 블로그에 노출된다.

```python
def publish_from_obsidian(note: str) -> str:
    return f"publish: {note}"
```

이 글의 `published` 속성을 `true`로 전환해 공개 경로를 검증한다.

자동 발행 검증: 두 번째이자 마지막 저장.

## 이미지와 위키링크 검증

![obsidian-blog-publish-test](/assets/img/posts/obsidian-publish-test/obsidian-blog-publish-test.png)

공개 위키링크의 블로그 URL 변환과 비공개 위키링크의 텍스트 변환을 검증했다.
