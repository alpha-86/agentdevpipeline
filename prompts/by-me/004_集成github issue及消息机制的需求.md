在hedge-ai项目中，建设了相对完整成熟的github issue能力，并且github issue也是整个hedge-ai项目研发流程管理的核心基础能力：
1. 从hedge-ai中迁移出整套涉及github issue，PR的能力，包括不局限于propmt、.claude/workflow、.git/workflow、python代码，cron脚本
2. github issue能力还涉及底层的跟claude的消息通信机制，请一并迁移过来。
3. telegram通信能力也一块迁移，注意相关key的配置要留好文档。
4. 注意在各个文档，尤其是README.md 中要讲清楚这部分的逻辑，解决什么问题，为什么采用这个手段解决问题，核心原则是什么等等。并且要通过流程图的形式，简洁明了的讲清楚流程。
