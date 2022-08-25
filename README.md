# pythonORM

## 1) models
    from app import db
    from app.models.base_entity import BaseEntity

    class Role(BaseEntity, db.Model):
        __tablename__ = "roles"
        roleid = db.Column(db.Integer, primary_key=True)
        rolename = db.Column(db.String(50), nullable=False, unique=True, index=True)
            self.data = data
            
### 1.2) relationship one to many
    class Parent(BaseEntity, db.Model):
        __tablename__ = "parents"
        parentid = db.Column(db.Integer, primary_key=True)
        childid = db.Column(db.ForeignKey('children.childid'))
        children = db.relationship("Child", cascade='all, delete-orphan')
        
    class Child(BaseEntity, db.Model):
        __tablename__ = "children"
        childid = db.Column(db.Integer, primary_key=True)
        parent = db.relationship("User", back_populates="children")
        
## 2) formulares
    class ExampleForm(FlaskForm):
        # désactiver CSRF pour les api
        class Meta:
            csrf = False
        exampleData = StringField('exampleData', validators=[])
        exampleData2 = StringField('exampleData2', validators=[DataRequired()])
        
## 3) mappers
    Créer les mapper pour passer des entités au dtos, et mettre à jours les entité à partir des forms.
    
## 4) services
    - des fonctions pour contacter la db : 
        - findOne => retourne une entité en fonction de son id
        - findOneBy => retourne une entité en fonction d'un paramètre passé (données d'une des colonnes)
        - findAll => retourne toutes les data
        - update => met à jours les donnés en DB
        - insert => insert des nouvelles donnée en DB
        - delete => delete une entrée en DB
     
## 5) controllers
    class ExampleController:
        # http://servername/path
        @app.route('/path', methods=['GET', 'POST'])
        def getAllData():
            return jsonify([example.get_json_parseable() for example in service.findAll()])
        # http://servername/path/1
        @app.route('/path/<int:dataid>', methods=['GET', 'POST'])
        def getAllData(dataid):
            return jsonify(service.findOne().get_json_parseable())
