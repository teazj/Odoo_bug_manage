# Odoo快速入门与实践 技术研发篇

在了解了**Python**的使用,**PostgreSQL**的使用以及**Odoo的简介**以后,我们就开始进入详细介绍技术研发的篇章.

* Odoo作为一款技术完善,功能强大的开源ERP产品,除了能够**提供常规的模块功能**之外,还**提供了二次开发环境**,本篇就来详细介绍二次开发的技术.

本篇将会按照**bug管理系统**的案例进行介绍,从简单功能到最终成为可用的完善功能.

* 依次介绍**模型**,**视图**,**数据导入导出,****ORM的使用**等相关知识.
* 通过本章学习,读者将可以**进行Odoo的二次开发**.

本篇(技术研发篇)在介绍过程中涵盖了所有的Odoo开发技术.

* 针对本篇,本书为读者提供了源码,**不过建议读者能够自己动手编写和测试代码**(实在不行可以对着源码进行修改),以加深理解.

***

## 目录


[TOC]

## 讲解视频地址



## gibhub地址





# 自建应用入门

在Odoo的开发过程中,**创建自己的模块是非常重要的**. 

* 前面已经提到过: **不建议直接修改源码**.

* 所以即便是修改已有的模块,也最好是新建一个模块,然后**继承**已有的模型进行扩展增强.

在admin用户的登录界面里,为什么设置前面的**菜单**称为**应用**而不是叫做模块呢? 

* 这是因为**模块**和**应用**本身就是不同的,应用是一个独立的系统,比如HR,CRM等,而模块这只是一组较为独立的功能,比如HR(应用)的招聘模块.
* 虽然招聘这个功能较为独立,但是很少有公司使用一个只有招聘功能的系统,但却有很多公司使用HR系统,这就是**应用**和**模块**的区别.
* 一般来讲,**应用**在Odoo里面有一个顶级菜单,而**很多模块只是在这些顶级菜单的下面增加的子菜单或动作**,这也是本书经常将模块称为**插件模块**的原因--因为模块往往已经是存在与应用中的插件了.

在本章中,我们将创建自己的第一个应用,并且在这个应用过程中介绍Odoo自建应用的主要流程和节点.

对于本次的项目,我们先做一个**bug管理系统**,通过Odoo来完成一个**bug提交**,**bug状态修改**等功能的模块,希望能够以此**了解创建自建模块的步骤**.

前面已经介绍过,**Odoo的整体架构是MVC分层设计的**,所以在实现bug管理系统的过程中,我们会接触到**model层**,**view层**,**controller层**,然后再设置本项目的访问**控制器**.

完成本章后,我们能够了解Odoo的基本构造,并可以重新开始体验一个项目的过程.



## 使用脚手架创建新模块

将**一组独立的功能按照不同的模块插件进行设计**是Odoo的一个特点,这样可以方便新增一些特性,也便于进行功能的迭代开发.

* 要了解一个模块的结构,可以通过其文件`__manifest__.py`来了解,该文件中列出了包含哪些视图,模型和演示数据,并且还可以配置本模块说明等基本信息,每个模块都必须包含这个文件.

前文中已经提到过,**不建议直接修改已有的代码,而是需要自建一个新的模块**.

* 我们只要自己配置好一个第三方的模块存放路径,并在 odoo.conf(配置文件)中进行声明

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806105729915-852108657.png)

* 使用如下命令创建模块: `python odoo-bin scaffold bug_manage myaddons`

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806110302739-1392065433.png)

* 下面来看看该模块的文件结构: 

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806110715728-2131716423.png)

* 此时打开`__manifest__.py`文件,可以看到里面是以**字典形式存放的数据**(一个{}),下面我们对文件内各个关键字(或者称为参数)的意义进行解释

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806112149673-1772892916.png)

* 我们根据自己的需求,只调整调整前面的几个参数即可,其他使用文件给出的默认值即可.

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806112608333-4704919.png)

## 安装和更新模块

我们已经创建了自己的模块,虽然没有进行业务逻辑和视图的开发,但是现在已经可以安装到Odoo了.

* 在初期了解Odoo的阶段,建议各位读者每进行一小步都及时进行测试,这样便于及时发现问题(测试不一定是"高大上"的,直接点击查看效果测试,或者直接输出print(),就是最简单粗暴的但是非常有效的测试,更加专业的测试应该个测试工程师去做)

所以本节首先介绍如何安装模块以及如何升级,并且介绍服务器的开发模型.

**安装模块是在前端完成**的,我们使用admin用户登录Odoo系统并按照以下步骤进行操作:

1. 点击 **设置** 界面右下角的 **激活开发者模式** 进入开发者模式.
2. 在 **应用** 界面点击左侧的 **更新应用列表** 按钮, 在弹出的对话框中点击 **更新** 按钮.
3. 然后搜索框中搜索bug,进行安装

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806114300902-1123939687.png)

如果后续对本模块进行了修改,那么可以继续使用该方法,只是到时候图表右下角会出现**升级**按钮,点击升级即可,也是要先更新应用列表.

 ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806115056679-1762236727.png)

因为Odoo服务只在启动的时候对Python代码加载过一次,所以如果**修改了Python代码**,则需要重新启动Odoo.

* 更为安全的方式时在重启服务的时候,加上更新的参数: `python odoo-bin -d 数据库名字 -u 要更新模块的名称`
* 当然,如果把 `-u` 替换为 `-i`,这样就可以安装模块了,对于Odoo11来说,还是在前端页面安装给更为方便一些.

注意: 如果希望在修改了Python代码之后不重启服务器就能让修改起作用,那么可以**使用Odoo的服务器开发模式**,只需要加上一个参数 `-dev=all`即可

* 在服务器开发模式下,每当我们保存Python文件时,服务器都会重新加载代码,这样就极大的加快了开发周期(其实不是很推荐)

下面我们通过一个小例子来查看升级的功能,我们为bug管理应用添加一个图标

* 我们需要`bug_manage`项目下创建目录`\static\description`,并将图标命名为`icon.png`

* 点击 **更新应用列表**,既可以看到这个新增的图标

  ![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806120610257-1452063990.png)

  

## 模型

我们已经在Odoo安装了自己的**模块**(module),现在可以添加自己的**模型**(models)了.

* 模型可用于**描述业务对象**,如订单,凭证等. (所有的对象都是可以使用字段来抽象信息化表示的)
* 模型是**通过继承Odoo模板的Python类(odoo.models.Model)进行增强扩展**来实现的.
* 创建模型后,Odoo会通过ORM引擎在数据库自动创建表.

我们的模型要完成的任务也比较简单,只是去维护bug列表.

* 每个bug均包含描述信息和是否完成的标示
* 后续将再来慢慢添加一些bug关闭等功能

### 创建模型

我们在`models`文件夹下创建`bugs.py`文件,然后在里面编辑代码,如下: 

```python
from odoo import fields, models, api


class Bugs(models.Model):
    _name = "bm.bug"
    _description = "bug"
    name = fields.Char(string='bug简述', required=True)
    detail = fields.Text(size=150)
    is_closed = fields.Boolean(string="是否关闭")
    close_reason = fields.Selection([("changed", "已修改"), ("cannot", "无法修改"), ("delay", "推迟"), ],
                                    string="关闭理由")
    user_id = fields.Many2one('res.users', string="负责人")
    follower_ids = fields.Many2many('res.partner', string='关注者')
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806151006142-1958572939.png)

关于模型的定义会在后面介绍,暂时可以将其看成是字段.

### 常用属性

从上面的例子中,我们可以看到,字段里面有多种属性,此处统一对常用的属性做一些介绍

* **string**: 在前端界面看到的字段名称,默认是字段的技术名称(技术名称就是`__manifest__.py`中的name).
* **required**: 默认是False,如果设置成True,则在创建记录时该字段不允许为空.(只是在前端页面的限制)
* **help**: 在前端使用时作为提示信息. (鼠标悬停的时候会给出提示信息)
* **index**: 布尔类型,默认为False. 如果是True,则会在数据库的该字段上创建索引.

### 保留字段

在模型里面,有一些字段是系统保留的,作为开发人员不能修改这些字段,这些保留字段具体如下:(这些字段是在模型定义的没有定义的,但是Odoo会创建表的时候自动加上,所以是客观存在的)

* **id**: 这是记录的唯一标识
* **create_date**: 记录创建的日期
* **create_uid**: Many2one类型,创建该记录的用户
* **write_date**: 记录的最后修改日期
* **write_uid**: Many2one类型,记录的最后修改用户
* **_last_update**: 该字段并不会实际存储值,在这里仅起到并发检查的作用

如果要查看以上字段的具体值,

* 可以在前端的开发者模式下,通过debug(臭虫按钮)的**查看元数据**选项查看数据明细
* 也可以直接在数据库中查看 bm_bug 数据表

**注意:** **name字段是模型里面的特殊字段**,在默认情况下该字段的值可用来在搜索和引用时代表一行记录.

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806225152116-2030236434.png)

###  模型继承

前面的章节,我们已经通过新建模型创建了Bugs模型. 在我们的引用中还有一个与bug是many2many关系的关注者,关注者就是关注bug的人,我们准备继承`res.partner`进行修改.

前面**新建的模型是通过Python类**来完成的,**扩展和增强已有模型也是通过Python类**来完成的.

Odoo提供了三种模型的继承机制,具体如下: 

* **经典继承**: 允许子类修改父类定义的方法,字段,也允许新增字段和方法.

  * 只需要使用 `_inherit`,默认`_name`字段与继承的模型一致(也就保证了是同一张数据表)

* **原型继承**: 和经典继承一样,只不过数据表是新建了一张数据表.

  * 需要使用`_inherit`和`_name`, `_name`和继承的模型`_name`不一致(所以在数据库中会复制原来的内容,在新建一张数据表)
  * **不推荐使用这种方式,因为会造成数据的冗余**

* **委派**: 将子类中新增的字段与父类中的字段进行关联,相当于保留了父类的字段和方法. 

  * 需要一个"外键字段", 只需要使用`_inherits`(注意: 后面有s)

    

我们选择**经典继承**方式来继承使用`res.partner`类,仍然是在models文件下创建类`followers.py`,并且编辑代码: 

```python
from odoo import models, field, api


class Follower(models.Model):
    _inherit = 'res.partner'  # 继承字段,声明要继承类的_name
    bug_ids = field.Many2many('bm.bug', string="bug")  # 新增字段
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806162402238-1105859849.png)

我们创建了两个类,但是不要忘记在 `models/__init__.py`文件中引入这两个新文件.

* 这是Python语法习惯的要求,如果不在此处,则Odoo将无法发现这两个文件.
* 我们应该在`__init__.py`文件内增加如下代码

```python
from . import bugs
from . import follower
```

注意: 应该修改了内置的`res.partner`,所以重新启动Odoo服务器会报错

* 解决方法: `python odoo-bin -c odoo.conf -u bug_manage` 启动时候加上`-u 要更新的模块`



## 视图

前面已经创建了**模型**,我们还需要**前端界面**,本节就来介绍**视图**.

* 注意: 在还没有配置视图时候,安装了应用在前端是不会显示的
* 如果都是使用默认的tree,search,form,那么配置一个menuitem和action即可

**视图是通过XML文件来定义的**,**前端框架(QWeb)会解析XML文件然后生成HTML文件**提供给浏览器执行.

视图的基本元素: 

* 菜单(menuitems)
* 动作(action)
* 列表视图(tree)
* 搜索视图(search)
* 表单视图(form)

我们通过后台的`views`文件夹下的XML文件来创建前端视图. 现在,我们就为bug管理系统应用创建视图.

### 新增菜单

我们先来创建bug管理系统的用户界面,需要在`views`文件夹下新建文件`bugs.xml`,并编辑如下代码

```xml
<odoo>
    <data>
        <!--动作窗口可以理解为一个桥梁    视图 <= 动作 => 菜单-->
        <record model="ir.actions.act_window" id="bug_manage.action_window">
            <field name="name">bug_manage window</field>
            <field name="res_model">bm.bug</field>
            <field name="view_mode">tree,form</field>
        </record>

        <!--顶级菜单-->
        <menuitem name="bug管理系统" id="bug_manage.menu_root"/>
        <!--二级菜单-->
        <menuitem name="bug管理" id="bug_manage.menu_1" parent="bug_manage.menu_root"/>
        <!--三级菜单  ==> 菜单和动作联系-->
        <menuitem name="bug列表" id="bug_manage.menu_1_list" parent="bug_manage.menu_1"
              action="bug_manage.action_window"/>
    </data>
</odoo>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806174224635-1592376595.png)

上述代码说明: 

* 注意XML是按顺序解释的,所有**动作窗口**必须要定义在**菜单**之前,否则会报错
* 上面是比较经典的定义视图的方式,这里使用的都是默认的tree,search,form,如果暂时不能理解,就先记住

我们需要在`__manifest__.py`的`data`中声明新增的`bugs.xml`文件(注意: 但凡是新增的xml和csv文件,都是需要在`__manifest__.py`中`data`字段中进行声明)

```python
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
    ],
```

然后如果需要看到效果的话,还需要设置一下安全权限(这里不理解不要紧,先照做),在编辑`security\ir.model.access.csv`,添加如下代码

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_bm_bug,bug_manage.bm_bug,model_bm_bug,,1,1,1,1
```

如果你使用 `-dev=all`参数,或者直接重启服务器,可以看到下图界面

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806175856790-1700047069.png)

因为我们所用的是系统生成的**列表视图**,所以显示的信息只有一个`name`字段

*  之前我们说过`name`是特殊字段(注意是`name`不是`_name`,后者是model的唯一标识),可以用来代表一条记录
*  但是如果仅仅只有这个字段,使用起来很不方便,我们需要更多字段字段信息,就需要创建自己的`tree`视图

### 创建列表(tree)视图

视图数据都是存储在数据库`ir.ui.view`模型中

* 若要向这个模型中新增之间的视图,则需要我们在XML文件中使用`<record>`元素
* 系统会在模块安装后解析这些XML文件,将`<record>`元素中的内容插入到模型中

下面我们仍然在`views/bugs.xml`文件中新增该列视图代码

```xml
        <!--自定义列表(tree)视图-->
		<record model="ir.ui.view" id="bug_manage.list">
            <field name="name">bug_manage list</field>
            <field name="model">bm.bug</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="name"/>
                    <field name="is_closed"/>
                    <field name="user_id"/>
                </tree>
            </field>
        </record>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806182815920-2114697204.png)



### 业务文档表单(form)视图

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806183529017-768999859.png)

我们在此直接跨过了**普通表单视图**的操作介绍,其实普通表单视图与前面介绍的列表视图非常相似,只是将`<tree>`和`<list>`互换一下.

**业务表单视图**就是在**普通表单视图**的基础上新增了`<header>`和`<sheet>`两个元素,我们还是在`views/bugs.xml`文件内增加如下代码

```xml
        <record model="ir.ui.view" id="bug_manage.form">
            <field name="name">bug_manage form</field>
            <field name="model">bm.bug</field>
            <field name="arch" type="xml">
                <form>
                    <header>
                        <!--这里的 button的name对应于未来后台的方法-->
                        <button name="do_close" type="object" string="关闭bug"/>
                    </header>
                    <sheet>
                        <group name="group_top" col="2">
                            <field name="name"/>
                            <field name="user_id"/>
                            <field name="is_closed"/>
                        </group>

                        <group name="group_right">
                            <field name="close_reason"/>
                            <field name="follower_ids"/>
                        </group>
                        <notebook>
                            <page string="详细内容">
                                <field name="detail"/>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806215145995-584618102.png)

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806212734249-101422370.png)

### 搜索(search)视图

到目前为止,我们的应用已经包含了**列表视图**和**表单视图**,而且都做了一些优化,但是现在还存在一个问题: 如果列表的记录变多了,查看起来不是很方便,我们还需要**搜索功能**还辅助提高效率.

在没有增加**搜索视图**之前,列表视图的右上方已经存在一个搜索框,这是Odoo自动添加的基于`name`字段的搜索视图,也就是说只能通过`name`(这里再次体现了`name`作为特殊字段的用途)

下面就来增加一个**搜索视图**,使**列表视图**可以基于`name`,`is_closed`,`user_id`进行搜索,仍然是在`views/bugs.xml`中添加代码

```xml
        <!--搜索视图-->
        <record model="ir.ui.view" id="bug_manage.search">
            <field name="name">bug_manage search</field>
            <field name="model">bm.bug</field>
            <field name="arch" type="xml">
                <search>
                    <field name="name"/>
                    <field name="is_closed"/>
                    <field name="user_id"/>
                </search>
            </field>
        </record>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806223334049-275570332.png)

**搜索视图**往往会和**预定义筛选条件**一起使用,这部分内容将会**结合后端视图**一起介绍.

### 视图继承

前面我们已经介绍了模型的继承,同样,**Odoo也支持对视图进行继承操作**.

* 视图的继承也是在XML代码中开发的
* 使用`inherit_id`属性引用被继承的视图,然后就可以在子视图中进行增强扩展.

结合我们的应用,关注者就算在`res.partner`模型的基础之上增加bug列表(bug_ids)字段的,所以关注者的视图也继承自`res.partner`视图进行修改.(模型是继承的,视图也是继承的就合情合理了)

现在,**第一步**就是要确定具体继承自哪一个视图(需要知道该视图的XML ID),进入 **设置 | 用户界面 | 视图**,搜索`res.partner`查看视图对应的外部ID

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200806231725288-267058712.png)

**第二步**需要找到具体的**锚点**,以此来确认我们的`bug_ids`最终会加载视图的哪个位置.

* 通常是寻找一个有`name`属性的元素
* 这里我们以 `<field name="mobile">`元素作为锚点

确定好要**继承视图的外部ID**和**找到对应的锚点**,我们可以开始进行视图继承了. 新建`views/follower.xml`文件并 编辑代码

```xml
<odoo>
    <data>
        <!--现在只是在 res.partner的表单中加入一个 bug_ids 的字段-->
        <record model="ir.ui.view" id="bug_manage.follower_form">
            <field name="name">follower_form</field>
            <field name="model">res.partner</field>
            <field name="inherit_id" ref="base.view_partner_form"/>
            <field name="arch" type="xml">
                <field name="mobile" position="after">
                    <field name="bug_ids"/>
                </field>
            </field>
        </record>

        <record model="ir.actions.act_window" id="bug_manage.follower_action_window">
            <field name="name">follower_action_window</field>
            <field name="res_model">res.partner</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem name="follower管理" id="bug_manage.follwer_menu" parent="bug_manage.bug_menu_root"/>

        <menuitem name="follower列表" id="bug_manage.follwer_menu_list" parent="bug_manage.follwer_menu"
                  action="bug_manage.follower_action_window"/>

    </data>
</odoo>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807094734997-1125402016.png)

代码说明: 

* `<field name="inherit_id" ref="继承视图的XML ID" />` 这是视图继承必须有的
* 这些选择`<field name>`中的`name`进行定位,其实还可以通过`<XPath>`进行定位,这个在后面会讲到

在`__manifest__.py`中引入此文件,更新应用后,可以看到

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807095538186-1769161367.png)

## 业务逻辑

在了解了**模型**和**视图**以后,下面就需要关注的就是一些**逻辑的具体处理**.

现在我们来实现**关闭bug**按钮的逻辑,逻辑在Python类中可以使用方法来完成,在文件`models/bugs.py`的Bugs类中增加如下代码

```python
    @api.multi
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807111658405-315261597.png)

更新应用后,打开一个bug(没有可以新建),点击**关闭bug**按钮,会发现**是否关闭**复选框已被选中.

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807111914429-1642592843.png)

## 安全性配置

Odoo可以通过**安全性配置**来设定到**菜单级**和到**模型级**的权限,可以具体到操作的查看,编辑和删除等明细操作,本节我们就来介绍一下Odoo的安全性配置.

### 访问控制

我们一直使用admin用户进行开发测试,**其实,目前普通用户还不能正常使用bug管理系统**,因为我们**还没有对该系统做任何访问设置**(在Odoo12开始,admin也需要做权限设置才能访问)

要想查看访问控制相关的信息,需要登录前端并进入 **设置 | 安全 | 访问列表** 页面.

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807113406387-747926267.png)

上图我们可以看到**模型**与**安全组**的对应关系,以及其具备的**增删改查**的具体权限.

这些访问权限数据全部存储在`ir.model.access`模型中,在我们的项目中,可以通过文件在系统启动时写入该模型.

* 因为我们是使用脚手架创建的项目,所以项目的`security`路径下已经默认创建了一个文件: `ir.model.acccess.csv`
* 注意: `模型名.csv`这是是规定,不能修改,这个CSV文件会将记录写入对应的模型中

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807115341622-1884287686.png)

修改完成后不要忘记在`__manifest__.py`中添加该csv文件

```python
    'data': [
        # 注意: 权限控制文件要放在开头
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bugs.xml',
        'views/follower.xml',
    ],
```

这里还没有创建**权限组**,如果要进行进行权限演示的话,需要在后面讲到创建权限组在进行演示.

注意: 除了模型了访问控制,还有**行级访问规则**,其具体的记录是存放在`ir.rule`模型中的,关于这点也是后面再说.

### 网页和控制器

Odoo还提供了一个**Web开发框架**,可**用于实现与后端功能高度集成的网站功能**.

* 我们在本节将会开发简单的网站网页用于显示我们的bug列表,是用户可以通过URL(`http://<serverhost>:8069/bug_manage`)访问我们的页面
* 本节只做最基本的介绍,更深入的内容会在第11章进行详细介绍

**Web控制器是负责网页转发的组件**,具体在技术上就是`http.Controller`类中定义的方法,这些方法绑定了终端页面的URL.

* 当URL被访问时,控制器代码就会执行相应的操作将HTML呈现给用户.
* 对于HTML的渲染,Odoo提供了**QWeb模板引擎**.

应用的控制器代码都放在`/controllers`文件夹下,在此目录中使用系统默认创建的文件`controllers.py`,编辑如下代码

```python
from odoo import http


class Bug(http.Controller):
    @http.route('/bug_manage')
    def bug_manage(self, **kw):
        bugs = http.request.env['bm.bug']  # 获取 bm.bug 记录集
        domain_bug = [('is_closed', '=', False)]  # 搜索条件
        bugs_open = bugs.search(domain_bug)  # 返回符合搜索条件的记录集
        return http.request.render('bug_manage.bugs_templates', {'bugs_open': bugs_open})
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807143100391-1711882121.png)

上面最后使用了`return http.request.render('bug_manage.bugs_templates',{})`,那么接下来我们就来创建`bugs_template`这个`QWeb`模板

```xml
<odoo>
    <data>

        <template id="bugs_templates" name="bug">
            <div class="container">
                <h1>未关闭的bug</h1>
                <t t-foreach="bugs_open" t-as="bug">
                    <div class="row">
                        <span t-field="bug.name"/>
                    </div>
                </t>
            </div>
        </template>
    </data>
</odoo>
```

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807144741100-1237794167.png)

保存上述XML代码,不要忘记加入`__manifest__.py`文件中,然后更新应用,访问`http://localhost:8069/bug_manage`,可以看到下图效果

![](https://img2020.cnblogs.com/blog/1517575/202008/1517575-20200807144959783-85534186.png)

## 总结

本章我们创建了一个bug管理模块,介绍了应用从创建到升级的全流程,并且按照模型,视图,业务逻辑对应用进行了介绍.

读者应该掌握了

* 应用项目的基本架构
* 知道如何 调整Python代码和XML文件以创建自己想要的界面
* 能够了解Odoo中继承的应用

本章还介绍了应用的安全性配置,包括访问控制,网页及控制器,读者应该能够根据需求进行权限配置

# 自建应用进阶

## 模型

## 字段

## 模型关系与复杂字段

## 更多模型继承机制

## 视图

## 总结

# 文件相关数据操作

## 外部ID

## 导入导出数据

## 模块数据

## 总结

# ORM API基础

## 常用装饰器



## ORM内置方法




## 数据导入导出方法

## 通信API

## 总结

# ORM: 业务逻辑处理

## 向导

## 更多ORM API用法

## 对记录集的操作

## 总结

# 创建网站

## 第一个页面

## 前端页面渲染

## 权限控制

## 总结

# 后端视图

## 菜单项和窗口动作

## 表单视图

## 视图字段

## 按钮

## 看板视图

## 其他类型的视图

## 总结

# QWeb

## 客户端QWeb

## 报表

## 服务器端QWeb

## 总结

# 与外部系统的集成

## Python客户端调用

## 客户端应用程序开发

## ERPpeek客户端

## OdooRPC库

## 总结
