# CRUD shop

## POST /shops

# body:
{
    "address": "my street 1234",
    "manager": "Roberto carlos"
 }

# response:
# 201:
{
    "id": 1,
    "address": "my street 1234",
    "manager": "Roberto carlos",
    "movies": []

}

# 422:
{
    "detail": ["mensaje de error"]
}

#-------------------------------------

# GET /shops

# response:
# 200:

[
    {
        "id": 1,
        "address": "my street 1234",
        "manager": "roberto carlos",
        "movies": []    
    },
    {
        "id": 2,
        "address": "my street 3423",
        "manager": "ronaldinio",
        "movies": []    
    }
]

#-------------------------------------

# GET /shops/1

# response
# 200:

{
    "id": 1,
    "address": "my street 1234",
    "manager": "roberto carlos",
    "movies": []
}

# 404

{
    "detail": ["sop no encontrado"]
}

#-------------------------------------

# PUT /shops/1
# body

{
    "address": "my street 1234 - updated",
    "manager": "Roberto carlos"
}

# Response

# 200
{
    "id": 1,
    "address": "my street 1234 - updated",
    "manager": "roberto carlos",
    "movies": []
}

# 400
{
    "details": ["shop no encontrado"]
}

# 422
{
    "details": ["datos invalidos"]
}

#-------------------------------------

# DELETE /shops/1
# response

# 204 
# (no content)

# 404
{
    "details": ["shop no encontrado"]
}

#-------------------------------------
#-------------------------------------
#-------------------------------------

# CRUD Movies

# POST /movies
# body
{
    "name": "Buscando a Kill Bill",
    "director": "Tarantino",
    "gender": ["action", "comedy"],
    "shop": 1
}

# response:
# 201:
{
    "id": 1,
    "name": "Buscando a Kill Bill",
    "director": "Tarantino",
    "gender": ["action", "comedy"],
    "shop": 1,
    "rent": "false"
}

# 422:
{
    "detail": ["Datos invalidos"]
}

# 404:
{
    "detail": ["shop no encontrado"]
}

#-------------------------------------

# GET /movies
# 200:

[
	{
		"id": 1,
		"name": "Buscando a Kill Bill",
		"director": "Tarantino",
		"gender": ["action", "comedy"],
		"shop": 1,
		"rent": "false"
	},
	{
		"id": 2,
		"name": "Titanic",
		"director": "James Cameron",
		"gender": ["drama", "romance"],
		"shop": 5,
		"rent": "true"
	}
]

#-------------------------------------

# GET /movies/1

# response
# 200:
{
    "id": 1,
	"name": "Buscando a Kill Bill",
	"director": "Tarantino",
	"gender": ["action", "comedy"],
	"shop": 10,
	"rent": "false"
}

# 404:
{
    "detail": ["movie not found"]
}

#-------------------------------------

# PUT /movies/1
# body:
{
    "name": "Kill Bill parte 1",
    "director": "Tarantino",
    "gender": ["action"],
    "shop": 1
}

# response
# 200:
{
    "id": 1,
    "name": "Kill Bill parte 1",
    "director": "Tarantino",
    "gender": ["action"],
    "shop": 1,
    "rent": "false"
}

# 404:
{
    "details": ["Movie no encontrada"]
}

# 422:
{
    "detail": ["Datos invalidos"]
}

#-------------------------------------

# DELETE /movies/1
# 204 
# (no content)

# 404
{
    "details": ["movie no encontrada"]
}

#-------------------------------------
#-------------------------------------
#-------------------------------------

# endpoints adicionales

# consultar todas las movies por shop
# GET /shop/1/movies

# response:
# 200:

[
    {
		"id": 1,
		"name": "Kill Bill",
		"director": "Tarantino",
		"gender": ["action"],
		"shop": 1,
		"rent": "false"
	},
	{
		"id": 3,
		"name": "Pulp Fiction",
		"director": "Tarantino",
		"gender": ["drama"],
		"shop": 1,
		"rent": "true"
	}
]

# 404
{
    "details": ["shop no encontrada"]
}

#-------------------------------------

# consultar todas las movies disponibles para alquilar por shop
# GET /shops/1/movies/available

# response
# 200

[
    {
        "id": 1,
        "name": "Buscando a Kill Bill",
        "director": "Tarantino",
        "gender": ["action", "comedy"],
        "shop": 1,
        "rent": "false"
    }
]

# 404
{
    "details": ["shop no encontrada"]
}

#-------------------------------------

# Cambiar de shop una movie
# PUT /movies/1

# body
{
	"name": "Kill Bill",
	"director": "Tarantino",
	"gender": ["action"],
	"shop": 5,
}

# response
{
	"id": 1,
	"name": "Kill Bill",
	"director": "Tarantino",
	"gender": ["action"],
	"shop": 5,
	"rent": "false"
}

# 404 
{
    "details": ["movie no encontrada"]
}

# 422
{
    "details": ["datos invalidos"]
}

#-------------------------------------

# obtener movies por nbname, gender o director
# GET /movies?name=kill&director=tarantino&gender=action

# response
# 200

[
    {
        "id": 1,
		"name": "Kill Bill",
		"director": "Tarantino",
		"gender": ["action"],
		"shop": 1,
		"rent": "false"
    }
]

#-------------------------------------

# GET /movies?name=kill

# response
# 200
[
	{
		"id": 1,
		"name": "Kill Bill",
		"director": "Tarantino",
		"gender": ["action"],
		"shop": 1,
		"rent": "false"
	}
]

#-------------------------------------

# GET /movies?director=cameron
[
	{
		"id": 2,
		"name": "Rapidos y furiosos",
		"director": "James Cameron",
		"gender": ["drama", "romance"],
		"shop": 5,
		"rent": "true"
	}
]