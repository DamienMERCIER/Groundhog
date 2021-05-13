D_SRC	=	./src/

NAME	=	groundhog

all:	$(NAME)
$(NAME)	:
			cp $(D_SRC)main.py ./
			mv main.py groundhog
			chmod +x groundhog

clean:
	@rm -f $(NAME)

fclean: clean

re: fclean all

.PHONY: all clean fclean re