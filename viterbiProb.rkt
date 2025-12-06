(define (viterbiProb
          emission k switchPr p1 p2)
  (cond
    [(null? (cdr emission))
     1]
    [#t
     (letrec 
         ([take (lambda (lst n)
                 (if (or (zero? n) (null? lst))
                     '()
                     (cons (car lst) (take (cdr lst) (- n 1)))))]
          [loop
           (lambda (EM K swPr P1 P2) ; KKKKKK
             ; return the complement of the probability 
             (if (= K 1)  ; base case: first emission only
                 (let ((is_inverse (if (= (car EM) 0) #f #t))
                       (c_p1 (- 1 p1))
                       (c_p2 (- 1 p2)))
                   (list (list p1 (* 0.5 (if is_inverse c_p1 p1)))
                         (list p2 (* 0.5 (if is_inverse c_p2 p2)))))
                 ; KKKKKK BELOW - Maybe I need to add another conditional where the mf is actually just the last thing, when K is equal to k
                 (letrec ((two_pairs (loop (cdr EM) (- K 1) swPr P1 P2)) ;gets two pairs of F or B paired with their probabilities
                       (most_likely (maxPair two_pairs))                 ;gets the most likely last coin 
                       (second_likely (if (equal? most_likely (car two_pairs))
                                          (car (cdr two_pairs))
                                          (car two_pairs))))          ;gets second likely coin with its probability
                   (let ((is_ml_p1 (if (= (car most_likely) p1) #t #f)) ;Is Most likely p1 or not?
                          (is_inverse (if (= (car EM) 1) #f #t))
                          (c_p1 (- 1 p1))
                          (c_p2 (- 1 p2))       ; is it 0 or not
                         )
                     (if is_ml_p1
                         (list (list p1
                                     (max
                                      (* (car (cdr second_likely)) switchPr (if is_inverse c_p1 p1)) ; V(B) x switching x (inverse or not of p1, depending on the emission)
                                      (* (car (cdr most_likely)) (- 1 switchPr) (if is_inverse c_p1 p1)))
                                     ) ; V(F) x not_switching x (inverse or not of p1, d on em)
                               (list p2
                                     (max
                                      (* (car (cdr most_likely)) switchPr (if is_inverse c_p2 p2))
                                      (* (car (cdr second_likely)) (- 1 switchPr) (if is_inverse c_p2 p2))))
                                     )
                         (list (list p1
                                     (max
                                      (* (car (cdr second_likely)) (- 1 switchPr) (if is_inverse c_p1 p1)) ; V(F) x not_switching x (inverse or not of p1, d on em)
                                      (* (car (cdr most_likely)) switchPr (if is_inverse c_p1 p1)))
                                     ) 
                               (list p2
                                     (max
                                      (* (car (cdr most_likely)) (- 1 switchPr) (if is_inverse c_p2 p2))
                                      (* (car (cdr second_likely)) switchPr (if is_inverse c_p2 p2))))
                                     ) ;V(B) x switching x (inverse or not of p2, depending on the emission)
                               )))))])
       ; KKKKKK; KKKKKKBELOW
              (define fixed-emission (reverse (take emission k)))
       (car (cdr (maxPair (loop fixed-emission k switchPr p1 p2)))))]))

