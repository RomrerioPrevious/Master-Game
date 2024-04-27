# Master game

Master game is a website for remote play of the Dungeons and Dragons tabletop role-playing game. In this game, the player can fight monsters and move around the cells. The player can either die in a battle with a mob or kill it. In order to play the game, the player must register and create a character for whom he will play.

### Creators

- [Roman](https://github.com/RomrerioPrevious) - TeamLead
- [Dmitry](https://github.com/dima117216) - FullStack
- [Vitalya](https://github.com/LooKing070) - FullStack

## How to install

Install poetry with the command:
```
pip install poetry
```
Install all dependencies with the command:
```
poetry install
```
Run it with the command:
```
poetry run main.py
```

## Functions and files

First of all, to start the game, the player must register and log in to his account. This is implemented in the authification_controller.py file in the register_page, register_user, create_user and authenticate_user functions. 
There is registration function:

```python
@app.route("/registration", methods=["POST"])
def register_user():
    data = request.form
    email = data["email"]
    password = data["password"]
    try:
        service.get_user_by_email(email)
    except Exception:
        password = hash_password(password)
        user = User(email=email, username=data["username"]password=password,
                    age=int(data["age"]), status="user", sheets=[])
        service.add_user(user)
        return redirect("/")
    except BaseException as ex:
        Logger.write_error(ex)
    return redirect("/registration")
```

The main work with characters is implemented in the character_controller.py file: functions from this file can create a character, update it, delete it, and get it from the form.
For example, there is creating character function:

```python
@app.route("/pers", methods=["POST"])
def create_character():
    user_id = int(request.cookies.get("user_id"))
    user = user_service.get_user_by_id(user_id)
    character = CharacterSheet()
    character_service.add_character(character)
    user["sheets"].append(character)
    UserService().update_user(user)
```

The controllers folder also contains the files game_controller.py, which controls the game process, graphql_controller.py, which controls work with graphql, and first_page_controller.py, which controls work with the first page. The /master_game/models/character folder contains files containing armor classes, weapons, character stats and sheets. The /master_game/services folder contains services that are used to work with databases, characters, users, and so on.
For example there is delete_character function from character_service.py:

```python
def delete_character(self, id: int) -> None:
    self._cash_service.delete(id)
    character = self.get_character(id=id)
    for weapon_id in character.weapons:
        weapon = self._session.query(Weapon).filter_by(Weapon.id == weapon_id).first()
        if weapon.counter - 1 == 0:
            self._session.delete(weapon)
        else:
            weapon.counter -= 1
    armor = self._session.query(Armor).filter_by(id=character.armor).first()
    if armor.counter - 1 == 0:
        self._session.delete(armor)
    else:
        armor.counter -= 1
    self._session.delete(character)
    if self.commit:
        self._session.commit()
    delete = f"user with id={character.id}"
    ic(delete)
```